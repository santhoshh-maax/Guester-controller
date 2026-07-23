import cv2
import mediapipe as mp
import serial
import serial.tools.list_ports
import time

def connect_to_esp32():
    """Scans for available COM ports and connects to the first one found."""
    ports = serial.tools.list_ports.comports()
    for port in ports:
        # Looking for common identifiers for ESP32/USB-Serial adapters
        if "USB" in port.description or "Serial" in port.description:
            try:
                print(f"✅ Found device: {port.device} ({port.description})")
                ser = serial.Serial(port.device, 9600, timeout=1)
                time.sleep(2)  # Wait for connection to stabilize
                return ser
            except Exception as e:
                print(f"⚠️ Could not open {port.device}: {e}")
    return None

# Initialize serial
ser = connect_to_esp32()
if not ser:
    print("⚠️ ESP32 not detected — Running in camera-only mode")

# Initialize MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

def count_fingers(hand_landmarks):
    """Counts fingers by comparing tip y-coordinates to knuckle y-coordinates."""
    tips = [8, 12, 16, 20] # Index, Middle, Ring, Pinky
    fingers = 0
    # Thumb check (using x-coordinates)
    if hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x:
        fingers += 1
    # Other finger checks
    for tip in tips:
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            fingers += 1
    return fingers

print("📷 Camera started... Show your hand!")

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb)

        if result.multi_hand_landmarks:
            for hand in result.multi_hand_landmarks:
                fingers = count_fingers(hand)
                
                # Serial communication logic
                if fingers == 1:
                    command = b'1'
                elif fingers == 2:
                    command = b'2'
                else:
                    command = b'0'
                
                if ser:
                    ser.write(command)
                
                print(f"🖐️ Fingers: {fingers} | Command: {command.decode()}")
                mp_draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)

        cv2.imshow("Hand Gesture Control", frame)

        if cv2.waitKey(1) == 27: # Press 'ESC' to exit
            break
finally:
    cap.release()
    cv2.destroyAllWindows()
    if ser:
        ser.close()
        print("🛑 Serial connection closed.")
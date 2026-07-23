
import cv2
import mediapipe as mp
import serial
import time

import serial.tools.list_ports

# 🔌 Try to connect to ESP32
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


try:
    ser = connect_to_esp32()
    time.sleep(2)
    print("✅ Serial connected to ESP32")
except:
    ser = None
    print("⚠️ ESP32 not connected — Running in camera-only mode")

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

print("📷 Camera started... Show your hand")


def count_fingers(hand_landmarks):
    tips = [8, 12, 16, 20] # thumb - 4, index - 8, middle - 12, ring - 16, pinky - 20
    fingers = 0

    for tip in tips: #example index rasied Tip = y=100 Joint = y=160 100 <160 True Finger Count =1
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            fingers += 1

    return fingers


while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Failed to capture frame")
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #Convert BGR → RGB
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks:
            fingers = count_fingers(hand)

            print("🖐️ Detected fingers:", fingers)

            if fingers == 1:
                print("👉 Command: LED ON")
                if ser:
                    ser.write(b'1')

            elif fingers == 2:
                print("👉 Command: LED 2 ON")
                if ser:
                    ser.write(b'2')
            elif fingers == 3:
                print("👉 Command: LED 3 ON")
                if ser:
                    ser.write(b'3')

            else:
                print("👉 Command: ALL OFF")
                if ser:
                    ser.write(b'0')

            mp_draw.draw_landmarks(frame, hand)

    else:
        print("No hand detected")

    cv2.imshow("Hand Gesture Control", frame)

    if cv2.waitKey(1) == 27:
        print("🛑 Exiting program")
        break

cap.release()
cv2.destroyAllWindows()

if ser:
    ser.close()


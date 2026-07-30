# ✋ Hand Gesture Controlled LED System using MediaPipe & ESP32 [![Sponsor](https://img.shields.io/badge/Sponsor-GitHub-db61a2?style=flat&logo=github-sponsors)](https://github.com/sponsors/santhoshh-maax)     [![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/N4N51YFMS9)


A real-time hand gesture recognition system that uses **MediaPipe**, **OpenCV**, and **Python** to detect the number of fingers shown to a webcam and control LEDs connected to an **ESP32** through serial communication.

This project demonstrates how computer vision can be integrated with IoT devices for touchless control applications.

---

# 📖 Project Overview

The system captures live video from a webcam and detects hand landmarks using Google's **MediaPipe Hands** solution. Based on the number of fingers detected, commands are sent to an ESP32, which controls three LEDs.

This project is useful for learning:

- Computer Vision
- Hand Gesture Recognition
- Serial Communication
- ESP32 Programming
- Human-Computer Interaction

---

# ✨ Features

- ✋ Real-time Hand Gesture Recognition
- 📷 Live Webcam Detection
- 🤖 MediaPipe Hand Tracking
- 💡 Control 3 LEDs using Gestures
- 🔌 Automatic ESP32 COM Port Detection
- ⚡ Serial Communication
- 🖥️ Camera-only mode if ESP32 is not connected

---

# 🛠️ Hardware Components

- ESP32 Development Board
- 3 LEDs
- 3 × 220Ω Resistors
- Breadboard
- Jumper Wires
- USB Cable

---

# 💻 Software Used

- Python 3.x
- OpenCV
- MediaPipe
- PySerial
- Arduino IDE

---

# 📂 Repository Structure

```text
Hand-Gesture-Control/
│
├── esp32_code/
│   └── esp32_code.ino
│
├── main.py
├── test.py
├── main.spec
├── .gitignore
└── README.md
```

---

# ⚙️ Working Principle

1. Open the webcam using OpenCV.
2. Detect hand landmarks using MediaPipe.
3. Count the number of raised fingers.
4. Send a command to the ESP32 through Serial.
5. ESP32 turns ON the corresponding LED.

---

# 🖐️ Gesture Commands

| Fingers Detected | ESP32 Command | Action |
|-----------------|--------------|--------|
| ☝️ 1 Finger | `1` | LED 1 ON |
| ✌️ 2 Fingers | `2` | LED 2 ON |
| 🤟 3 Fingers | `3` | LED 3 ON |
| Others / No Hand | `0` | All LEDs OFF |

---

# 🔌 Circuit Connections

| ESP32 Pin | Component |
|-----------|-----------|
| GPIO 2 | LED 1 |
| GPIO 4 | LED 2 |
| GPIO 5 | LED 3 |
| GND | Common Ground |

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/Hand-Gesture-Control.git
```

---

## Install Python Libraries

```bash
pip install opencv-python mediapipe pyserial
```

---

## Upload ESP32 Code

1. Open Arduino IDE.
2. Open the code inside the `esp32_code` folder.
3. Select your ESP32 board and COM port.
4. Upload the sketch.

---

## Run the Python Program

```bash
python main.py
```

---

# 📊 How It Works

```text
Webcam
   │
   ▼
OpenCV
   │
   ▼
MediaPipe Hand Detection
   │
   ▼
Finger Counting
   │
   ▼
Python
   │
Serial Communication
   │
   ▼
ESP32
   │
   ▼
LED Control
```

---

# 📷 Example

| Gesture | Result |
|----------|--------|
| ☝️ 1 Finger | LED 1 ON |
| ✌️ 2 Fingers | LED 2 ON |
| 🤟 3 Fingers | LED 3 ON |
| ✋ Open Hand / No Hand | All LEDs OFF |

---

# ⚠️ Notes

- The program automatically searches for the ESP32 COM port.
- If the ESP32 is not connected, the application runs in **camera-only mode**.
- Ensure no other application is using the serial port.
- A webcam is required for gesture detection.

---

# 🚀 Future Improvements

- Control Home Appliances
- Bluetooth Communication
- Wi-Fi-Based IoT Control
- Custom Gesture Recognition
- Gesture-Based Robot Control
- Home Automation Dashboard

---

# 👨‍💻 Author

**Santhosh P**

B.E. Computer Science and Engineering

Mount Zion College of Engineering and Technology

👉 **[Sponsor me on GitHub](https://github.com/sponsors/santhoshh-maax)**

---

# ⭐ Support

If you found this project useful, please consider giving this repository a **⭐ Star**.

---

# 📜 License

This project is developed for educational and learning purposes.

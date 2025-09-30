# 🤖 Vision-Based Robotic Pick-and-Place System (YOLOv8 + FastAPI)

## 📌 Project Overview

This project demonstrates a complete end-to-end **AI + Robotics pipeline** where a vision system detects objects in real time using a deep learning model (YOLOv8) and then commands a simulated robotic arm to "pick" and "place" those objects. The system mimics how real-world autonomous robots perceive, decide, and act.

It is designed to be easy to understand, extend, and integrate with actual robotic hardware (via ROS2 or other controllers). This project is ideal for showcasing practical robotics AI skills to employers.

---

## 🧠 System Architecture Overview

The project follows a typical **robotics intelligence loop** used in real-world systems:

```
+-------------------+      +--------------------+      +--------------------+      +------------------+
|   📷 Perception    | ---> |   🧠 Decision       | ---> |   🦾 Action         | ---> |  🔁 Feedback      |
|  (YOLO + OpenCV)  |      | (Target Selection) |      | (Arm Control API)  |      | (Next Frame)     |
+-------------------+      +--------------------+      +--------------------+      +------------------+
```

* **Perception:** Detects objects using YOLOv8 from a live camera feed.
* **Decision:** Chooses a target and computes the pick coordinates.
* **Action:** Sends commands to a (simulated) robotic arm for pick-and-place.
* **Feedback:** Repeats continuously for autonomous real-time operation.

---

## 🧠 Detailed Workflow – Stage by Stage

### 1. 📷 Perception – Vision and Object Detection

**File:** `detector/object_detector.py`

* Captures live video frames from a webcam using **OpenCV**.
* Each frame is passed to a pre-trained **YOLOv8** model from the `ultralytics` library.
* YOLO identifies known objects (e.g., "person", "bottle", "cup") with **bounding boxes**, **labels**, and **confidence scores**.
* Detected objects are drawn with **green rectangles** and labels.
* A **red dot** marks the center of the first detected object — representing the target “pick” point.

🔁 This process repeats for every frame, enabling continuous real-time perception.

---

### 2. 🧠 Decision – Target Selection and Command Preparation

**File:** `main.py`

* Processes the detections and selects a target object (currently the first one).
* Calculates the object's **center coordinates (x, y)** — where the robotic arm should pick it up.
* Prepares pick-and-place commands with these coordinates.

💡 This stage acts as the "brain" — interpreting sensory input and deciding the next action.

---

### 3. 🦾 Action – Robotic Arm Control (Simulated)

**Files:** `api/server.py`, `controller/arm_controller.py`

* A **FastAPI microservice** simulates a robotic arm controller.
* The main loop sends HTTP requests to the API:

  * `/pick` – simulate picking the object at the calculated coordinates.
  * `/place` – simulate placing the object at a new position.
* The `ArmController` class mimics real robot actions, printing execution logs.

🛠️ In a real system, this would send commands to physical hardware or a ROS2 simulation.

---

### 4. 🔁 Feedback – Continuous Real-Time Loop

* Once an action is complete, the system returns to perception.
* The cycle repeats: capture → detect → decide → act → repeat.
* This closed-loop control is fundamental in robotics.

---

## 📂 Project Structure

```
robotic_vision_pick_place/
│
├── detector/
│   ├── __init__.py
│   └── object_detector.py      # YOLOv8 detection and drawing
│
├── controller/
│   ├── __init__.py
│   └── arm_controller.py       # Robotic arm logic (simulated)
│
├── utils/
│   ├── __init__.py
│   └── camera_stream.py        # Camera handling
│
├── api/
│   ├── __init__.py
│   └── server.py               # FastAPI microservice for arm control
│
├── main.py                     # Main loop: vision → decision → action
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run the Project

### 1. 📦 Install Dependencies

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
pip install ultralytics opencv-python fastapi uvicorn requests
```

### 2. 🦾 Start the Robotic Arm API

Run this in **Terminal 1**:

```bash
uvicorn api.server:app --reload
```

✅ Output:

```
Uvicorn running on http://127.0.0.1:8000
```

### 3. 📷 Start the Vision System

Run this in **Terminal 2**:

```bash
python main.py
```

✅ You should see:

* A **camera window** with live feed
* **Green boxes** around detected objects
* A **red dot** marking the pick location
* Terminal logs like:

```
✅ Picking object at coordinates (320, 220)...
📦 Object picked!
🚀 Placing object at (420, 270)...
✅ Object placed successfully!
```

Press **`q`** to exit.

---

## 📊 What This Demonstrates

This project illustrates the internal workings of real-world robotics systems:

| Stage         | What Happens                 | Real-World Equivalent           |
| ------------- | ---------------------------- | ------------------------------- |
| 📷 Perception | Camera + YOLO detect objects | Vision sensors & ML models      |
| 🧠 Decision   | Choose object + plan action  | Motion planning / control logic |
| 🦾 Action     | Send pick/place commands     | Robotic arm controller          |
| 🔁 Feedback   | Repeat loop                  | Continuous autonomous operation |

This is the **core intelligence loop** behind warehouse robots, industrial manipulators, and autonomous systems.

---


## 🚀 Future Extensions

* 🤖 Connect to a real robotic arm or ROS2 simulation
* 🧠 Add object filtering and task prioritization
* 🏃‍♂️ Implement trajectory planning for smoother movements
* 📊 Build a dashboard to visualize detections and robot state

---

## 📜 Summary

This project is a foundational demonstration of how **AI and robotics** work together. It integrates computer vision, decision-making, and robotic control into one continuous loop — the essence of any autonomous robotic system.

With this project, you demonstrate practical skills in:

* Deep learning and real-time vision (YOLOv8, OpenCV)
* Robotics integration and control logic
* Microservice-based robot control (FastAPI)
* End-to-end AI system design

It’s an excellent portfolio project for applying to **robotics companies and AI startups**, showing that you understand not only machine learning but also how to embed it into autonomous robotic systems.

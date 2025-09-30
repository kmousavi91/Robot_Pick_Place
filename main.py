import cv2
import requests
from detector.object_detector import ObjectDetector
from utils.camera_stream import CameraStream

# Initialize components
detector = ObjectDetector()
camera = CameraStream()

API_URL = "http://127.0.0.1:8000"

while True:
    frame = camera.get_frame()
    detections = detector.detect(frame)
    frame = detector.draw_boxes(frame, detections)

    # If objects detected, pick the first one
    if detections:
        obj = detections[0]
        x_center = (obj["bbox"][0] + obj["bbox"][2]) // 2
        y_center = (obj["bbox"][1] + obj["bbox"][3]) // 2

        # Send pick command
        requests.post(f"{API_URL}/pick", json={"x": x_center, "y": y_center})
        requests.post(f"{API_URL}/place", json={"x": x_center + 100, "y": y_center + 50})

    cv2.imshow("Robotic Vision System", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()


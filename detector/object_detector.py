import cv2
from ultralytics import YOLO

class ObjectDetector:
    def __init__(self, model_path="yolov8n.pt", conf=0.5):
        self.model = YOLO(model_path)
        self.conf = conf

    def detect(self, frame):
        results = self.model.predict(frame, conf=self.conf)
        detections = []
        for result in results[0].boxes.data.tolist():
            x1, y1, x2, y2, conf, cls = result
            detections.append({
                "bbox": [int(x1), int(y1), int(x2), int(y2)],
                "confidence": conf,
                "class_id": int(cls),
                "class_name": self.model.names[int(cls)]
            })
        return detections

    def draw_boxes(self, frame, detections):
        for det in detections:
            x1, y1, x2, y2 = det["bbox"]
            cls_name = det["class_name"]
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
            cv2.putText(frame, cls_name, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)
        return frame


import cv2

class CameraStream:
    def __init__(self, src=0):
        self.cap = cv2.VideoCapture(src)

    def get_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            raise RuntimeError("Failed to capture frame")
        return frame

    def release(self):
        self.cap.release()
        cv2.destroyAllWindows()


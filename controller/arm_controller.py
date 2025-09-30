import time

class ArmController:
    def __init__(self):
        pass

    def pick_object(self, x, y):
        print(f"✅ Picking object at coordinates ({x}, {y})...")
        time.sleep(1)
        print("📦 Object picked!")

    def place_object(self, x, y):
        print(f"🚀 Placing object at ({x}, {y})...")
        time.sleep(1)
        print("✅ Object placed successfully!")


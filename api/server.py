from fastapi import FastAPI
from pydantic import BaseModel
from controller.arm_controller import ArmController

app = FastAPI()
arm = ArmController()

class Coordinates(BaseModel):
    x: int
    y: int

@app.post("/pick")
def pick_object(coords: Coordinates):
    arm.pick_object(coords.x, coords.y)
    return {"status": "picked", "coords": coords.dict()}

@app.post("/place")
def place_object(coords: Coordinates):
    arm.place_object(coords.x, coords.y)
    return {"status": "placed", "coords": coords.dict()}


import gradio as gr
from ultralytics import YOLO
import cv2


model = YOLO("best.pt")


def detect_lane(image):

    results = model(image)

    output = results[0].plot()

    return output



interface = gr.Interface(

    fn=detect_lane,

    inputs=gr.Image(
        type="numpy",
        label="Upload Road Image"
    ),

    outputs=gr.Image(
        label="Detected Lane"
    ),

    title="AI Lane Detection System",

    description=
    "YOLO based lane detection project"

)


interface.launch()
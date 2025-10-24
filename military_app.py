
import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np

st.title("Military Object Detection using YOLOv8")
st.markdown("Upload an image to detect military objects")

# Load your trained YOLO model
model_path = "/content/drive/MyDrive/Final_Military_project/military_safety_yolov8/weights/best.pt"
model = YOLO(model_path)

# Class names (from your YOLO dataset)
class_names = ["weapon", "military_truck", "military_vehicle", "military_artillery", "military_warship"]

# Upload image
uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file).convert("RGB")
    st.image(img, caption="Uploaded Image", use_column_width=True)

    with st.spinner("Detecting..."):
        # Predict using YOLO
        results = model.predict(img, conf=0.3)

        # Plot image with bounding boxes
        result_img = results[0].plot()
        st.image(result_img, caption="Detection Result", use_column_width=True)

        # Display detected classes with confidence
        st.subheader("Detected Classes")
        if len(results[0].boxes.data) == 0:
            st.write("No objects detected")
        else:
            for box in results[0].boxes.data:
                cls = int(box[-1])          # Class ID
                conf = box[-2].item()       # Confidence
                st.write(f"{class_names[cls]} (Class ID: {cls}), Confidence: {conf:.2f}")

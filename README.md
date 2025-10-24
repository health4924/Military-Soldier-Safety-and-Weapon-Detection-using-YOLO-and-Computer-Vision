# 🛡️ Military Soldier Safety and Weapon Detection using YOLOv8 and Streamlit

## 🚨 Project Summary
This project implements a state-of-the-art Computer Vision system using **YOLOv8** for **real-time object detection and classification** in military and defense scenarios. The primary goal is to **enhance soldier safety and situational awareness** by accurately identifying potential threats (weapons, enemy combatants) while distinguishing them from non-threats. The system is deployed via a **user-friendly Streamlit web application**.

## 🎯 Domain & Problem Statement
The system addresses the need for robust, real-time surveillance to quickly **detect threats** (weapons, enemy soldiers) and **differentiate entities** (military vs. civilian) in dynamic, high-stress environments.

### Detected Classes (9 Total)
* `camouflage_soldier`, `soldier`
* `weapon` (Threat)
* `military_tank`, `military_truck`, `military_vehicle`
* `civilian`, `civilian_vehicle` (Non-Threats)
* `trench` (Defensive Structure)

### Business Use Cases
1.  **Military Surveillance & Threat Detection:** Real-time monitoring of conflict zones.
2.  **Soldier Safety & Alert Systems:** Instantaneous alerts regarding nearby threats.
3.  **Border Security:** Automated intrusion detection at checkpoints.
4.  **Combat Zone Analysis:** Tactical analysis, including identifying trenches and military assets.

---

## 📈 Model Performance and Results
The trained YOLOv8 model demonstrated production readiness with high accuracy and real-time inference speed.

| Metric | Result | Target Focus |
| :--- | :--- | :--- |
| **mAP** | **85%** | Overall model accuracy across all classes. |
| **Precision** | **88%** | Minimized False Positives (Correctly detected objects). |
| **Recall** | **83%** | High coverage of all actual objects in the scene. |
| **Threat Accuracy** | **92%** | Accuracy in classifying objects as 'Threat' vs. 'Non-Threat'. |
| **Inference Time**| **30 FPS** (on GPU) | Confirms **real-time capability** for field deployment. |

**Key Achievements:**
* **Weapons Detection:** Achieved **>90% precision and recall**, successfully overcoming the challenge of small object detection.
* **Robustness:** Performed well in diverse environments (urban clutter, forests, low-light).

---

## 💻 Project Setup and Usage

### Prerequisites
1.  **Python 3.8+**
2.  **Required Libraries:** Install using `pip`:
    ```bash
    pip install ultralytics opencv-python-headless streamlit numpy pandas
    ```

### Running the Streamlit Web App
To launch the user interface for prediction and visualization:
1.  Ensure the `best.pt` model is accessible.
2.  Run the following command in your terminal:
    ```bash
    streamlit run streamlit_app.py
    ```

### Accessing Deliverables
| Deliverable | Description |
| :--- | :--- |
| **Trained YOLO Model** | `best.pt` file, located in your repository (e.g., `military_safety_yolov8/weights/`). |
| **Streamlit Web Application** | `streamlit_app.py` file. |
| **Jupyter Notebook** | Contains complete code for data handling, training, and evaluation. |
| **Sample Outputs** | Images/videos with detected objects, saved under the `runs/predict/` directory. |
| **Performance Metrics Report** | `model_performance_report.csv` file. |

---

## 🛠️ Skills & Technical Tags
* **Python, Computer Vision, OpenCV, Streamlit**
* **Deep Learning:** YOLO object detection model.
* **Image Processing:** Resizing, contrast enhancement, and edge detection techniques (used in EDA/Preprocessing).

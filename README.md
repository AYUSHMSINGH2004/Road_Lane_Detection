# 🚘 AI-Based Road Lane Detection System using YOLOv8


<p align="center">

<img src="https://img.shields.io/badge/AI-Computer%20Vision-blue">
<img src="https://img.shields.io/badge/Model-YOLOv8-green">
<img src="https://img.shields.io/badge/Deployment-HuggingFace-orange">

</p>


# 📌 Project Overview


Road lane detection is an important Computer Vision task used in:

- Autonomous vehicles
- Advanced Driver Assistance Systems (ADAS)
- Intelligent Transportation Systems


This project presents an **AI-powered Road Lane Detection System** capable of detecting road lane markings from images using a trained **YOLOv8 object detection model**.


The complete pipeline includes:

- Dataset preparation
- XML annotation processing
- YOLO dataset conversion
- Deep learning experimentation
- YOLOv8 training
- Model evaluation
- Testing
- Deployment


---

# 🎯 Problem Statement


Traditional image processing based lane detection methods struggle in real-world environments because of:

- Lighting variations
- Shadows
- Complex backgrounds
- Road surface changes
- Perspective variations
- Curved lanes


The objective of this project was to develop a deep learning based system capable of detecting road lanes automatically.



---

# 🚀 Project Objectives


- Build an automated road lane detection system
- Explore traditional Computer Vision methods
- Experiment with CNN based segmentation
- Implement YOLOv8 object detection
- Evaluate model performance
- Deploy the trained AI model



---

# 📂 Dataset Information


## Dataset Source

**Kaggle Road Lane Detection Dataset**


Dataset structure:

```
dataset/

│

├── road_line_images/

│        └── Road Images (.jpg)


│

└── road_line_annotation/

         └── XML annotations
```


Dataset details:

| Parameter | Value |
|-|-|
| Total Images | 48 |
| Annotation Format | Pascal VOC XML |
| Class | road_line |
| Training Images | 38 |
| Validation Images | 10 |


The XML annotations were converted into YOLO compatible labels.



---

# 🛠️ Development Journey


# Phase 1: Traditional Computer Vision Approach


Initially, a classical OpenCV based lane detection system was developed.


Techniques used:

- Image resizing
- Grayscale conversion
- Gaussian filtering
- Edge detection
- Hough Line Transform


Pipeline:

```
Input Image

↓

Preprocessing

↓

Edge Detection

↓

Hough Transform

↓

Lane Detection
```


## Limitations

The approach failed because:

- Highly dependent on lighting conditions
- Poor performance with shadows
- Sensitive to noise
- Difficult for curved roads
- No feature learning capability



---

# Phase 2: CNN Based Lane Segmentation Approach


A CNN based segmentation model was implemented.


Workflow:

```
Input Image

↓

CNN Model

↓

Lane Mask Prediction

↓

Detected Lane Region
```


Technologies:

- PyTorch
- CNN Architecture
- BCEWithLogitsLoss


Challenges faced:

- XML parsing issues
- Annotation mismatch
- Mask generation problems
- Limited dataset size
- Poor segmentation accuracy


The segmentation approach was not suitable for final deployment.



---

# Phase 3: Final Solution - YOLOv8


After experimentation, YOLOv8 was selected as the final model.



## Why YOLOv8?


Advantages:

- Faster inference
- Automatic feature extraction
- Better performance on small datasets
- Easy deployment
- Real-time capable



Final pipeline:

```
Road Image

↓

YOLOv8 Model

↓

Lane Detection

↓

Prediction Output
```



---

# 🧠 Model Details


## Model Used

```
YOLOv8 Nano
```


## Training Method

Transfer Learning


A pretrained YOLOv8 model was fine-tuned on the road lane dataset.


Training configuration:

```
Epochs : 50

Image Size : 640

Optimizer : Adam
```


Dataset split:

```
Training : 38 Images

Validation : 10 Images
```



---

# 📁 Dataset Conversion Pipeline


Original format:

```
Pascal VOC XML
```


Converted format:

```
YOLO TXT


<class>

<x_center>

<y_center>

<width>

<height>
```



Final YOLO dataset:

```
yolo_dataset/


│

├── images/

│       ├── train/

│       └── val/


│

├── labels/

│       ├── train/

│       └── val/


└── data.yaml
```



---

# 📊 Model Evaluation


The trained model was evaluated using:

- Training loss
- Validation loss
- Precision
- Recall
- mAP
- Confusion Matrix



---

# 📈 Training Results


Training performance graphs:


![Training Results](https://res.cloudinary.com/dsvgl6yd5/image/upload/v1782820216/results_uzlte5.png)



The graphs include:

- Box loss
- Classification loss
- DFL loss
- Precision
- Recall
- mAP50
- mAP50-95



---

# Confusion Matrix


The confusion matrix evaluates:

- Correct lane detection
- False predictions
- Background classification


![Confusion Matrix](https://res.cloudinary.com/dsvgl6yd5/image/upload/v1782820215/confusion_matrix_rrtbkm.png)



---

# 🧪 Testing


Testing pipeline:

```
Input Image

↓

YOLOv8 Model

↓

Prediction

↓

Detected Output
```


Testing outputs:

```
testing_results/
```


Before and after comparisons:

```
before_after/
```



---

# 🌐 Deployment


The trained AI model is deployed as an interactive web application.



## Deployment Platform

**Hugging Face Spaces + Gradio**



## Live Demo


🔗 https://ayushmsingh2004-lane-detection-project.hf.space/



---

# Deployment Architecture


```
User

↓

Gradio Interface

↓

YOLOv8 Model

(best.pt)

↓

Inference Engine

↓

Lane Detection Output
```



---

# Application Features


✅ Upload road images  
✅ AI lane detection  
✅ YOLOv8 inference  
✅ Confidence control  
✅ Fast prediction  
✅ Cloud deployment  
✅ Interactive UI  



---

# 📦 Complete Project Backup


All project files are available here:


Google Drive:


🔗 https://drive.google.com/drive/folders/132H8g8l7yQhwkqDIY-Rw5QoefWdBNm1V?usp=drive_link



Contains:


```
before_after

lane_detection_results

project_results

road_dataset

yolo_dataset

runs

testing_results
```



---

# 🖥️ Technology Stack


## Programming

- Python


## Deep Learning

- YOLOv8
- PyTorch


## Computer Vision

- OpenCV


## Data Processing

- NumPy
- XML Parsing


## Deployment

- Hugging Face Spaces
- Gradio


## Development Environment

- Google Colab



---

# 📂 Project Structure


```
Lane-Detection-Project/


│

├── app.py

├── best.pt

├── requirements.txt


├── road_dataset/


├── yolo_dataset/


├── runs/


├── project_results/


├── testing_results/


└── before_after/
```



---

# ⚡ Installation and Usage


Clone repository:

```bash
git clone <repository-url>

cd Lane-Detection-Project
```


Install dependencies:

```bash
pip install -r requirements.txt
```


Run application:

```bash
python app.py
```



---

# 🔮 Future Improvements


- Larger road datasets
- Real-time video lane detection
- Lane departure warning system
- Vehicle trajectory estimation
- YOLO segmentation models
- Edge device deployment



---

# 🏆 Key Learnings


This project provided practical experience in:


- Computer Vision pipelines
- Dataset annotation processing
- XML to YOLO conversion
- Deep learning model training
- YOLO object detection
- Model evaluation
- AI deployment



---

# 👨‍💻 Author


## Ayush M Singh


**AI/ML Engineer | Computer Vision Developer**


Areas of Interest:

- Artificial Intelligence
- Machine Learning
- Deep Learning
- Computer Vision
- AI Deployment
- Autonomous Systems



---

# ⭐ Project Demo


Live Application:

https://ayushmsingh2004-lane-detection-project.hf.space/


---

# Acknowledgement


This project was developed using open-source Artificial Intelligence frameworks and contributions from the Computer Vision community.


Special thanks to:

- Ultralytics YOLO
- PyTorch
- OpenCV
- Hugging Face

for enabling this implementation.

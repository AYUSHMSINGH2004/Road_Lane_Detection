# 🚘 AI-Based Road Lane Detection System using YOLOv8

![Project Banner](project_results/sample_output.png)


## 📌 Project Overview

Road lane detection is an important Computer Vision task used in autonomous vehicles, Advanced Driver Assistance Systems (ADAS), and intelligent transportation systems.

This project focuses on developing an AI-powered road lane detection system capable of identifying road lane markings from images using deep learning.

The final system uses a trained **YOLOv8 object detection model** and provides an interactive web application where users can upload road images and receive lane detection predictions.

The complete pipeline includes:

- Dataset preparation
- XML annotation processing
- YOLO dataset conversion
- Model training
- Model evaluation
- Testing
- Deployment


---

# 🎯 Problem Statement

Traditional lane detection methods based on image processing often fail in real-world road environments because of:

- Lighting variations
- Shadows
- Complex backgrounds
- Road surface changes
- Perspective variations
- Curved lanes


The objective of this project is to build a reliable deep learning-based lane detection system that can automatically identify road lanes from images.


---

# 🚀 Project Objectives

The main objectives of this project are:

- Develop an automated road lane detection system
- Explore traditional computer vision approaches
- Implement deep learning-based detection
- Train a YOLOv8 model on road lane data
- Evaluate model performance
- Deploy the trained AI model as a web application


---

# 📂 Dataset Information


## Dataset Used

**Kaggle Road Lane Detection Dataset**


Dataset structure:


```
dataset/

│
├── road_line_images/

│       └── Road images (.jpg)


│
└── road_line_annotation/

        └── XML annotation files

```


Dataset details:

- Total images used: 48
- Annotation format: Pascal VOC XML
- Detection class:
    - road_line


The XML annotations contained lane coordinates which were converted into YOLO-compatible labels.


---

# 🛠️ Project Development Journey


## Phase 1: Traditional Computer Vision Approach (OpenCV)


Initially, a classical computer vision-based lane detection approach was explored.


Techniques used:

- Image resizing
- Grayscale conversion
- Gaussian filtering
- Edge detection
- Hough Line Transform


### Limitations:


The approach was not reliable because:

- Detection depended heavily on lighting conditions
- Lane markings were sometimes unclear
- Curved roads were difficult to detect
- Noise affected results
- No feature learning capability was available


Because of these limitations, a deep learning approach was explored.


---

# Phase 2: CNN Based Lane Segmentation Approach


A custom deep learning segmentation approach was attempted.


Workflow:


```
Input Road Image

        ↓

CNN Model

        ↓

Lane Mask Prediction

        ↓

Detected Lane Region

```


Technologies used:

- PyTorch
- CNN architecture
- BCEWithLogitsLoss


### Challenges faced:


- XML annotation parsing issues
- Image and annotation mismatching
- Floating point coordinate conversion problems
- Mask generation difficulties
- Small dataset size
- Poor segmentation output quality


The segmentation model did not produce satisfactory lane detection results.


---

# Phase 3: Final Solution - YOLOv8 Based Detection Model


After analyzing previous approaches, YOLOv8 was selected as the final solution.


## Why YOLO?


YOLO (You Only Look Once) is a real-time object detection algorithm.


Advantages:

- Faster inference
- Automatic feature extraction
- Better performance with limited datasets
- Simple training pipeline
- Easy deployment


Final architecture:


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


## Approach

Transfer Learning


A pretrained YOLOv8 model was fine-tuned on the road lane dataset.


Training configuration:

- Epochs: 30+
- Image size: 640
- Optimizer: Adam


Dataset split:


```
Training Images : 38

Validation Images : 10

```


---

# 📁 Dataset Conversion Pipeline


Original annotation format:


```
Pascal VOC XML

```


Converted into:


```
YOLO TXT Format


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


│

└── data.yaml

```


---

# 📊 Model Evaluation


The trained model was evaluated using:


## Training Metrics


Generated:

- Training loss graphs
- Validation metrics
- Precision
- Recall
- mAP scores


## Confusion Matrix


Used to analyze:

- Correct detections
- False detections
- Missed detections


Evaluation outputs:


```
project_results/

│

├── Training graphs

├── Accuracy curves

└── Confusion matrix

```


---

# 🧪 Testing


Testing workflow:


```
Input Image

       ↓

YOLO Model

       ↓

Prediction

       ↓

Detection Output

```


Testing results:


```
testing_results/

```


Before vs After comparison:


```
before_after/

```


---

# 🌐 Deployment


The final trained AI model has been deployed as an interactive web application.


## Deployment Platform

**Hugging Face Spaces + Gradio**


## Live Demo


🔗 https://ayushmsingh2004-lane-detection-project.hf.space/


Users can upload road images and receive AI-generated lane detection results.


---

# Deployment Architecture


```
User

 |

 ↓

Gradio Web Interface

 |

 ↓

YOLOv8 Trained Model

(best.pt)

 |

 ↓

Lane Detection Prediction

 |

 ↓

Processed Output Image

```


---

# Application Features


✅ Upload road images  
✅ AI-based lane detection  
✅ YOLOv8 inference  
✅ Adjustable confidence threshold  
✅ Fast image processing  
✅ Cloud-based deployment  
✅ Interactive user interface  


---

# 🖥️ Technology Stack


## Programming Language

- Python


## Deep Learning

- YOLOv8
- PyTorch


## Computer Vision

- OpenCV


## Data Processing

- NumPy
- XML Parsing


## Development Environment

- Google Colab


## Deployment

- Hugging Face Spaces
- Gradio


---

# 📦 Project Structure


```
Lane-Detection-Project/


│

├── app.py

├── best.pt

├── requirements.txt


│

├── road_dataset/


│

├── runs/

│       └── YOLO training results


│

├── project_results/

│       ├── graphs

│       └── confusion matrix


│

├── testing_results/


│

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


Possible improvements:


- Train on larger road datasets
- Real-time video lane detection
- Lane departure warning system
- Vehicle trajectory estimation
- YOLO segmentation models
- Edge device deployment


---

# 🏆 Key Learnings


Through this project, I gained practical experience in:


- Computer Vision pipelines
- Dataset annotation handling
- Deep learning model training
- YOLO object detection
- Model evaluation
- AI application deployment


---

# 👨‍💻 Author


## Ayush M Singh


**AI/ML Engineer | Computer Vision Developer**


### Areas of Interest:

- Artificial Intelligence
- Machine Learning
- Deep Learning
- Computer Vision
- AI Model Deployment
- Intelligent Transportation Systems


---

# ⭐ Project Demo


Try the live AI application:


🔗 https://ayushmsingh2004-lane-detection-project.hf.space/


---

# Acknowledgement


This project was developed using open-source AI frameworks and research contributions from the Computer Vision and Deep Learning community.

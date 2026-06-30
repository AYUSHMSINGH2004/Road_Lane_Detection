# 🚘 AI-Based Road Lane Detection System using YOLOv8


<p align="center">

<img src="https://img.shields.io/badge/AI-Computer%20Vision-blue">
<img src="https://img.shields.io/badge/Model-YOLOv8-green">
<img src="https://img.shields.io/badge/Deployment-HuggingFace-orange">

</p>


# 📌 Project Overview


Road lane detection is a critical Computer Vision task used in:

- Autonomous vehicles
- Advanced Driver Assistance Systems (ADAS)
- Intelligent transportation systems


This project presents an **AI-powered Road Lane Detection System** capable of detecting road lane markings from images using a trained **YOLOv8 object detection model**.


The complete pipeline includes:


- Dataset preparation
- XML annotation processing
- YOLO dataset conversion
- Deep learning experimentation
- YOLOv8 training
- Model evaluation
- Testing
- Web deployment



---

# 🎯 Problem Statement


Traditional image processing based lane detection methods struggle in real-world environments due to:


- Lighting variations
- Shadows
- Complex road backgrounds
- Perspective changes
- Curved roads
- Noise


The goal was to build a robust AI system capable of automatically detecting road lanes from images.


---

# 🚀 Project Objectives


The main objectives:


- Develop an automated lane detection system
- Explore classical Computer Vision techniques
- Experiment with CNN-based approaches
- Implement YOLOv8 object detection
- Evaluate model performance
- Deploy the trained model online



---

# 📂 Dataset Information


## Dataset Source


**Kaggle Road Lane Detection Dataset**


Dataset structure:


```
dataset/

│

├── road_line_images/

│       └── Road images (.jpg)


│

└── road_line_annotation/

        └── Pascal VOC XML files

```


Dataset details:


| Parameter | Value |
|-|-|
| Total Images | 48 |
| Annotation Format | Pascal VOC XML |
| Detection Class | road_line |
| Training Images | 38 |
| Validation Images | 10 |



The XML annotations were converted into YOLO format.



---

# 🛠️ Development Journey



# Phase 1: Traditional Computer Vision Approach


Initially, a classical OpenCV pipeline was developed.


Techniques:


- Image resizing
- Grayscale conversion
- Gaussian filtering
- Edge detection
- Hough Line Transform



Pipeline:


```
Image

↓

Preprocessing

↓

Edge Detection

↓

Hough Transform

↓

Lane Lines

```



## Limitations


The approach failed because:


- Highly dependent on lighting
- Poor performance on shadows
- Failed on complex backgrounds
- No learning capability
- Difficult on curved roads



Therefore, a deep learning approach was explored.



---

# Phase 2: CNN Based Lane Segmentation Approach


A CNN segmentation model was implemented.


Architecture:


```
Input Image

↓

CNN Network

↓

Lane Mask

↓

Detected Lane Region

```


Technologies:


- PyTorch
- CNN
- BCEWithLogitsLoss


Challenges:


- XML parsing issues
- Annotation mismatch
- Mask generation problems
- Limited dataset size
- Poor segmentation accuracy



The segmentation approach was not reliable enough for deployment.



---

# Phase 3: Final Solution - YOLOv8


After experimentation, YOLOv8 was selected as the final model.


## Why YOLOv8?


Advantages:


- Faster inference
- Better feature extraction
- Works well with limited datasets
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


## Model


```
YOLOv8 Nano
```


## Training Approach


Transfer Learning


A pretrained YOLOv8 model was fine-tuned using the road lane dataset.



Training configuration:


```
Epochs : 50

Image Size : 640

Optimizer : Adam

```



---

# 📁 Dataset Conversion


Original:


```
Pascal VOC XML

```


Converted:


```
YOLO TXT


<class>

<x_center>

<y_center>

<width>

<height>

```


Final structure:


```
yolo_dataset/


├── images/

│       ├── train/

│       └── val/


├── labels/

│       ├── train/

│       └── val/


└── data.yaml

```



---

# 📊 Model Evaluation



The model was evaluated using:


- Precision
- Recall
- mAP
- Training loss
- Validation loss
- Confusion matrix



## Training Performance Graphs


The following metrics were generated:


- Box loss
- Classification loss
- DFL loss
- Precision curve
- Recall curve
- mAP50
- mAP50-95



![Training Graphs](project_results/results.png)



---

# Confusion Matrix



The confusion matrix shows prediction performance between:


- road_line
- background



![Confusion Matrix](project_results/confusion_matrix.png)



Normalized confusion matrix:


![Normalized Confusion Matrix](project_results/confusion_matrix_normalized.png)



---

# 🧪 Testing


Testing pipeline:


```
Input Image

↓

YOLOv8 Model

↓

Detection

↓

Output Image

```



Results:


```
testing_results/

```


Before vs After:


```
before_after/

```



---

# 🌐 Deployment



The trained model is deployed as an interactive AI application.



## Platform


**Hugging Face Spaces + Gradio**



## Live Demo


🔗

https://ayushmsingh2004-lane-detection-project.hf.space/



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

Inference

↓

Detected Lane Output

```



---

# 📦 Project Backup


Complete project files:


Google Drive:


🔗

https://drive.google.com/drive/folders/132H8g8l7yQhwkqDIY-Rw5QoefWdBNm1V?usp=drive_link



Contains:


```
before_after

lane_detection_results

project_results

road_dataset

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



## Development


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


├── runs/

│      └── YOLO training results


├── project_results/

│      ├── graphs

│      ├── confusion matrix


├── testing_results/


└── before_after/

```



---

# ⚡ Installation



Clone repository:


```bash
git clone <repository-url>

cd Lane-Detection-Project

```



Install dependencies:


```bash
pip install -r requirements.txt

```



Run:


```bash
python app.py

```



---

# 🔮 Future Improvements


Possible improvements:


- Larger road datasets
- Video lane detection
- Real-time vehicle integration
- Lane departure warning
- YOLO segmentation
- Edge device deployment



---

# 🏆 Key Learnings


This project provided practical experience in:


- Computer Vision pipelines
- Annotation processing
- Dataset conversion
- Deep learning training
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


Try the deployed AI system:


https://ayushmsingh2004-lane-detection-project.hf.space/



---

# Acknowledgement


This project was developed using open-source Artificial Intelligence frameworks and contributions from the Computer Vision research community.

Special thanks to:


- Ultralytics YOLO
- PyTorch
- OpenCV
- Hugging Face


for enabling this implementation.

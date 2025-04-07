# 🌾 Semi-Automated Weed Detection System

A deep learning-based computer vision project that detects and highlights weeds in agricultural fields using image input. This semi-automated system assists farmers and agricultural bots in identifying weed-infested areas efficiently, saving cost and reducing excessive herbicide usage.

![Weed Detection Sample](./assets/weed-detection-example.png)

---

## 📌 Table of Contents

- [Introduction](#-introduction)
- [Features](#-features)
- [Workflow](#-workflow)
- [Technologies Used](#-technologies-used)
- [Installation](#-installation)
- [Usage](#-usage)
- [Results](#-results)
- [Future Scope](#-future-scope)
- [License](#-license)
- [Author](#-author)

---

## 🌱 Introduction

Modern agriculture faces challenges from unwanted weeds that reduce crop yields and require excessive manual effort or chemicals to eliminate. This project leverages computer vision and deep learning to semi-automate the process of weed detection, enabling smart, targeted intervention.

This system takes an image as input (from camera or dataset), detects weed regions, and highlights them with a dark pink boundary for easy visualization and action.

---

## ✨ Features

- Detects and highlights weeds in field images.
- Semi-automated: human validation possible before final action.
- Works in real-time or on static datasets.
- Highlights weed areas using dark pink bounding boxes or masks.
- Saves annotated output images for review or further processing.

---

## 🔄 Workflow

1. **Image Capture**  
   Images are captured from a mounted camera or uploaded from a dataset.

2. **Preprocessing**  
   Images are resized, normalized, and augmented (if needed).

3. **Weed Detection Model**  
   A trained deep learning model (e.g., YOLOv8, U-Net) is used to identify and classify weed regions.

4. **Post-processing**  
   Detected weed regions are outlined with a dark pink boundary or mask overlay.

5. **Output**  
   Annotated images are saved locally. Optionally, coordinates or labels are exported.

---

## 🧰 Technologies Used

- **Python 3**
- **OpenCV**
- **PyTorch / TensorFlow** (based on model)
- **YOLOv8** or **U-Net** (for segmentation or detection)
- **Matplotlib** / **Pillow** (for image handling)
- **LabelImg** or **Roboflow** (for annotation)

---

## 💻 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/semi-automated-weed-detection.git
cd semi-automated-weed-detection

python detect_weeds.py --input images/sample.jpg --output output/

python detect_weeds.py --realtime

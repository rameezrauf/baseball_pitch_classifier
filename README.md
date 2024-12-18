# Image Classification with TensorFlow

Welcome to the **Image Classification with TensorFlow** repository! This project involves building a deep learning model to classify images into different categories. The project includes data preprocessing, cleaning, and training a convolutional neural network (CNN) using TensorFlow. This project was created in Octiber, 2023. 
---

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Dataset](#dataset)
- [Model Architecture](#model-architecture)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Future Work](#future-work)
- [Contributions](#contributions)
- [Contact](#contact)

---

## Project Overview

This project focuses on:
1. Cleaning and organizing image datasets.
2. Training a convolutional neural network (CNN) for image classification.
3. Utilizing GPU acceleration for efficient model training.
4. Showcasing end-to-end deep learning workflows, from data preprocessing to model evaluation.

---

## Features

- **Automated Data Cleaning**: Identifies and removes corrupt or incompatible images.
- **GPU Optimization**: Configures TensorFlow for GPU-based training to avoid memory overflow.
- **Custom CNN**: Implements a convolutional neural network for robust classification performance.
- **Scalable Design**: Supports additional image categories with minimal changes.

---

## Dataset

The dataset is organized into subdirectories under the `data/` folder, where each subdirectory represents a class. Images are checked for compatibility during preprocessing to ensure data integrity.

### Preprocessing Steps:
1. Validate image formats using `cv2` and `imghdr`.
2. Remove incompatible or corrupt files.
3. Normalize and resize images for model training.

---

## Model Architecture

The project employs a custom convolutional neural network (CNN) built with TensorFlow. Key components include:
- **Convolutional Layers**: For feature extraction.
- **Pooling Layers**: To reduce dimensionality.
- **Fully Connected Layers**: For classification.
- **Dropout Layers**: To prevent overfitting.

---
## Future Work
- **Pitch Classification:** Classify what type of pitch was thrown (Slider, 2 seam-fastball, Curve, etc)
- **Video Classification:** Expand model to digest videos and increase accuracy
- **Dataset Expansion:** Incorporate more diverse datasets to improve generalization.
- **Model Optimization:** Experiment with transfer learning and pre-trained models.
- **Web Integration:** Build a web app for real-time image classification.

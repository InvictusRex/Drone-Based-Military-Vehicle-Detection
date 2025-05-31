# Drone-Based Real-Time Military Vehicle Detection Using YOLOv8 and YOLOv11 Architectures

This project presents an advanced object detection system for **real-time identification of military vehicles** from UAV-mounted cameras using YOLO-based deep learning models. We benchmark six model variants, YOLOv8n, v8s, v8m and YOLOv11n, 11s, 11m, to determine the optimal choice for **onboard drone deployment**, balancing detection accuracy with computational efficiency.

The models are evaluated on a curated multi-class aerial dataset featuring tanks, trucks, humvees, and armored vehicles, with an input resolution of 1024×1024 across all variants.

---

## ⚙️ System Overview

### Core Components

1. **Aerial Dataset Preprocessing**
   - Manual annotation and class balancing
   - Classes: `tank`, `truck`, `armored_vehicle`, `hummer`
   - Augmentations: HSV, blur, cutout, resizing

2. **YOLO Model Training**
   - Six variants trained independently
   - Optimizer: AdamW  
   - Input size: 1024×1024  
   - Epochs: 100  
   - IoU Threshold: 0.7  
   - Augmented P2 layer enabled (for small object sensitivity)

3. **Inference and Application**
   - Real-time bounding box detection at 30 FPS
   - Model integration on edge-compatible UAVs
   - Use-case: real-time reconnaissance, vehicle classification, or autonomous targeting

---

### 🔢 Model Configurations

| Variant     | Architecture               | GFLOPs | Deployment Suitability         |
|-------------|----------------------------|--------|---------------------------------|
| YOLOv8n     | CSPDarknet (C2f + PAN-FPN) | 8.1    | Ultra-lightweight drones        |
| YOLOv8s     | Medium-scale encoder       | 28.4   | Jetson Nano / Xavier NX         |
| YOLOv8m     | Extended feature backbone  | 78.7   | High-performance embedded edge  |
| YOLOv11n    | Custom PAN+Backbone        | 6.3    | Optimized for low-power UAVs    |
| YOLOv11s    | Intermediate architecture  | 21.3   | Balance of accuracy & efficiency|
| YOLOv11m    | Deeper spatial encoder     | 67.7   | Edge GPU (Jetson AGX, Xavier)   |

---

## 📊 Evaluation Summary

### Model Performance on Aerial Military Dataset

| Model       | GFLOPs | Precision | Recall | mAP@50 | mAP@50-95 | F1 Score | Accuracy |
|-------------|--------|-----------|--------|--------|------------|----------|----------|
| YOLOv8n     | 8.1    | 0.750     | 0.679  | 0.743  | 0.529      | 0.712    | 0.714    |
| YOLOv8s     | 28.4   | 0.787     | 0.727  | 0.746  | 0.558      | 0.756    | 0.757    |
| YOLOv8m     | 78.7   | 0.785     | 0.729  | **0.777** | **0.588**  | **0.766**| **0.767**|
| YOLOv11n    | 6.3    | 0.758     | 0.714  | 0.744  | 0.752      | 0.735    | 0.573    |
| YOLOv11s    | 21.3   | 0.758     | 0.716  | 0.745  | 0.550      | 0.736    | 0.574    |
| YOLOv11m    | 67.7   | **0.761** | **0.717** | 0.750  | 0.559      | 0.744    | 0.578    |

---

## ✅ Model Selection for Drone Deployment

The choice of model depends on the deployment scenario:

### 🔹 **Best Overall Detection Performance**
- **Model**: `YOLOv8m`
- **Why**: Highest mAP@50 (0.777), F1 (0.766), and accuracy (0.767)
- **Trade-off**: High computational load (78.7 GFLOPs); suitable for high-end edge GPUs (Jetson AGX Xavier, Orin)

### 🔹 **Best Lightweight Deployment**
- **Model**: `YOLOv11n`
- **Why**: Lowest GFLOPs (6.3), good balance of precision (0.758) and mAP@50 (0.744)
- **Use-case**: UAVs with strict power constraints (e.g., Jetson Nano, RPi + Coral)

### 🔹 **Balanced Performance and Efficiency**
- **Model**: `YOLOv8s` or `YOLOv11s`
- **Why**: Reasonable accuracy (F1 ~0.75), moderate GFLOPs (~20–28), low memory footprint
- **Use-case**: Mid-range edge devices; real-time inference with acceptable latency

---

## 🔬 Research Insights

- **YOLOv8m** is optimal when accuracy is paramount and compute is available.
- **YOLOv11n** and **YOLOv11s** are strong contenders for energy-efficient UAVs.
- Detection performance is consistent across architectures, but compute constraints significantly influence deployment feasibility.

---

## 🚧 Known Limitations

- Models show reduced performance under:
  - Occlusion
  - Similar background clutter
  - Low-light aerial imagery
- Dataset may lack diversity in angles and backgrounds for some classes (e.g., trucks)

---

## 🛠 Future Work

- Add thermal and night-vision variants to improve detection in low visibility
- Integrate tracking (e.g., DeepSORT) for target persistence
- Deploy real-world test flights using NVIDIA Jetson boards
- Quantize and prune selected models for faster inference and reduced power draw

---

## 📌 Conclusion

This project establishes a flexible, efficient, and scalable pipeline for **aerial vehicle detection**, suited for a wide range of embedded drone platforms. Whether you're optimizing for speed, accuracy, or edge deployment, our benchmark of YOLO variants provides a clear guideline for model selection.

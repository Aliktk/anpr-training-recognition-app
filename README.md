# 🚗 License Plate Detection System

This project implements a License Plate Detection System using **YOLOv8** and **EasyOCR**. The system detects and localizes license plates from vehicle images and performs OCR (Optical Character Recognition) to extract the text from the detected plates. The application can be run in CLI mode for real-time detection and can also be deployed as a web-based application using **Streamlit**.

---

## 📚 Table of Contents

- [🚗 License Plate Detection System](#-license-plate-detection-system)
  - [📚 Table of Contents](#-table-of-contents)
  - [✨ Features](#-features)
  - [📁 Project Structure](#-project-structure)
  - [Prerequisites ⚙️](#prerequisites-️)
  - [How to Run 🚀](#how-to-run-)
    - [Running the Detection System (CLI) 🖥️](#running-the-detection-system-cli-️)
  - [Running the Streamlit App 🌐](#running-the-streamlit-app-)
  - [Using the Streamlit App Features 🛠️](#using-the-streamlit-app-features-️)
  - [Configuration ⚙️](#configuration-️)
    - [Example Configuration:](#example-configuration)
  - [Example Usage 📋](#example-usage-)
    - [CLI Detection for Image 📷](#cli-detection-for-image-)
  - [Example Usage](#example-usage)
    - [CLI Detection for Video 🎥](#cli-detection-for-video-)
  - [Future Enhancements 🚀](#future-enhancements-)
  - [Acknowledgements 🙏](#acknowledgements-)
  - [Follow Us for Updates! 🌟](#follow-us-for-updates-)

---

## ✨ Features

- **YOLOv8-Based License Plate Detection**: Utilizes the YOLOv8 object detection model for accurate and fast license plate localization. 🎯
- **EasyOCR for Text Extraction**: Integrates EasyOCR to extract text from localized license plates. 📝
- **CLI Support**: Provides command-line functionality for detection on video files or images. 💻
- **Streamlit Integration**: Deploy a user-friendly web interface to upload and detect license plates interactively. 🌐
- **Custom Dataset**: The model is trained on a custom dataset using Roboflow for precise performance. 📊
- **Performance Logging**: Logs the detection process with detailed information and error handling. 📜

---

## 📁 Project Structure

```bash
.
├── README.md               # Project documentation
dataset/
├── train/
│   ├── images/
│   │   ├── image1.jpg
│   │   ├── image2.jpg
│   └── labels/
│       ├── image1.txt
│       ├── image2.txt
├── valid/
│   ├── images/
│   │   ├── image1.jpg
│   │   ├── image2.jpg
│   └── labels/
│       ├── image1.txt
|── logs/                   # Log files for detection process
├── runs/                   # Model checkpoints and result logs
├── models/                 # Pre-trained models or checkpoints
├── app/                    # Streamlit app code
├── detect_modified.py       # Main detection script with YOLOv8 and OCR
├── requirements.txt        # Python dependencies
└── config.yaml             # YOLOv8 model configuration


```

## Prerequisites ⚙️

Ensure you have the following installed:

- Python 3.8+ 🐍
- CUDA-enabled GPU (if you want to run it on GPU) 🖥️
- `easyocr`, `torch`, `ultralytics`, `opencv-python`, and `streamlit` Python libraries (refer to `requirements.txt`)

To install dependencies, run:

```bash
pip install -r requirements.txt

```

## How to Run 🚀

### Running the Detection System (CLI) 🖥️

You can run the License Plate Detection System in CLI mode by executing the following command:

```bash
python detect_modified.py model='ultralytics/runs/detect/train_model/weights/best.pt' source='path_to_video_or_image'

```

Replace `path_to_video_or_image` with the path to your input file (video or image). The detected license plates will be displayed, and OCR will be performed to extract the text.

## Running the Streamlit App 🌐

To interact with the detection system via a web interface, run the Streamlit app:

1. Navigate to the app directory where the `Main.py` file is located. 📁
2. Run the following command:

    ```bash
    streamlit run app/Main.py
    ```

This will launch the Streamlit web app on localhost. You can upload images or videos, and the app will detect and display the results, including the extracted license plate text. 📸

## Using the Streamlit App Features 🛠️

- **Upload Files:** 📤 Upload an image or video for real-time license plate detection.
- **View Detections:** 👀 Detected license plates will be displayed along with the extracted text from the plates.

---
Open your browser and go to the provided URL (usually localhost:8501) to interact with the app.

## Configuration ⚙️

You can modify the YOLOv8 configuration by updating the `config.yaml` file. Key configuration options include:

- **Model Path:** 📂 Define the path to the YOLOv8 model checkpoint.
- **Confidence Threshold:** 📊 Adjust the confidence threshold for detections.
- **Image Size:** 📏 Set the input image size for detection.

### Example Configuration:

```yaml
model: 'ultralytics/runs/detect/train_model/weights/best.pt'
imgsz: 640
conf: 0.25
iou: 0.45
max_det: 1000
device: 0
```

## Example Usage 📋

### CLI Detection for Image 📷

To run detection on an image file, execute the following command:

```bash
python detect_modified.py model='ultralytics/runs/detect/train_model/weights/best.pt' source='test_image.jpg'
```

## Example Usage

### CLI Detection for Video 🎥

To run detection on a video file, use the command below:

```bash
python detect_modified.py model='ultralytics/runs/detect/train_model/weights/best.pt' source='test_video.mp4'
```

## Future Enhancements 🚀

- **OCR Language Support:** Add support for multiple languages for OCR using EasyOCR. 🌍
- **Improved Post-processing:** Implement advanced post-processing to enhance OCR results on low-quality license plates. 🔧
- **Real-time Video Stream Support:** Extend functionality to support real-time detection from a video feed (e.g., a camera). 📹
- **Docker Support:** Add a Dockerfile to containerize the application for easy deployment. 🐳

## Acknowledgements 🙏

- **YOLOv8:** For the base model used for object detection.
- **EasyOCR:** For Optical Character Recognition.


## Follow Us for Updates! 🌟

Stay tuned for updates and enhancements to the License Plate Detection System! 

- **GitHub:** [Alitktk](https://github.com/Alitktk) – Check out the repository for the latest code and releases. ⭐️
- **Feedback:** Your feedback is important! Please raise issues or suggestions on GitHub.
- **Social Media:** Follow us on [Twitter]((https://www.twitter.com/engr_ali_nawaz)) and [LinkedIn](https://www.linkedin.com/in/ali-nawaz-khattak/) for the latest news and updates!

Thank you for your support! 💖

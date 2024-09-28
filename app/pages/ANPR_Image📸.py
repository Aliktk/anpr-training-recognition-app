import streamlit as st
from PIL import Image
import cv2
from ultralytics import YOLO
import easyocr

# Streamlit app title
st.title("🚗 Automatic Number Plate Recognition (ANPR)")

# File uploader widget
uploaded_file = st.file_uploader("Upload your image (jpg, jpeg, png):", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    try:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        
        # Convert and save the uploaded image
        image_rgb = image.convert("RGB")
        image_rgb.save("saved_image.jpg", format="JPEG")
        frame = cv2.imread("saved_image.jpg")

        # Load the YOLO model (ensure the model path is correct)
        model = YOLO("best.pt")

        # Perform plate detection
        results = model(frame, save=True)

        if len(results[0].boxes) == 0:
            st.subheader("No plate detected!")
        else:
            st.subheader("License Plate Detected!")
            reader = easyocr.Reader(['en'], gpu=True)
            
            # Process each detection
            for result in results[0].boxes.data.tolist():
                x1, y1, x2, y2, score, _ = result
                # Draw bounding box around the detected plate
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
                
                # Crop the detected plate
                cropped_img = frame[int(y1):int(y2), int(x1):int(x2)]
                cv2.imwrite('cropped_plate.jpg', cropped_img)
                
                # Display cropped license plate
                plate_image = Image.open('cropped_plate.jpg')
                st.image(plate_image, caption='Detected License Plate', use_column_width=True)
                
                # Convert cropped image for OCR
                easyocr_image = cv2.cvtColor(cropped_img, cv2.COLOR_BGR2RGB)
                ocr_results = reader.readtext(easyocr_image)
                
                if ocr_results:
                    # Extract text from OCR result
                    text, confidence = ocr_results[0][1], ocr_results[0][2]
                    st.write(f"**Extracted License Plate:** {text}")
                    st.write(f"**Confidence Score:** {confidence:.2f}")
                else:
                    st.write("No readable text detected in the license plate.")

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
else:
    st.info("Please upload an image to proceed.")

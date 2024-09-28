import easyocr
import cv2
from ultralytics import YOLO
import streamlit as st
from utils import update_csv
import tempfile
import os


st.title("🚗 Automatic Number Plate Recognition (ANPR) on Video")

# Create a file uploader widget for video input
uploaded_file = st.file_uploader("Upload your video (mp4, avi):", type=["mp4", "avi"])

# Initialize session state
if "value_set" not in st.session_state:
    st.session_state.value_set = True

if st.session_state.value_set:

    if uploaded_file is not None:
        try:
            st.video(uploaded_file)

            # Create a temporary file for the uploaded video
            temp_file = tempfile.NamedTemporaryFile(delete=False)
            temp_file.write(uploaded_file.read())
            temp_file.close()

            # Load the YOLO models
            model = YOLO('yolov8x.pt')  # Pre-trained YOLO model for tracking
            lp_detector = YOLO("best.pt")  # Custom model for license plate detection
            reader = easyocr.Reader(['en'], gpu=True)

            # Open video file
            cap = cv2.VideoCapture(temp_file.name)
            if not cap.isOpened():
                st.error("Error: Could not open video.")
                raise Exception("Video could not be opened")

            # Get video properties
            fps = int(cap.get(cv2.CAP_PROP_FPS))
            frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

            # Define codec and create VideoWriter object for saving the output video
            output_path = 'output_video.mp4'
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # MP4 codec
            out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

            frame_nbr = 0
            ret = True
            with st.spinner("Processing the video..."):
                while ret:
                    ret, frame = cap.read()

                    # Process every 10th frame
                    if ret and frame_nbr % 10 == 0:
                        results = model.track(frame, persist=True)
                        
                        for result in results[0].boxes.data.tolist():
                            if len(result) == 7:  # Ensure the result has exactly 7 elements
                                x1, y1, x2, y2, id, score, label = result
                            else:
                                continue  # Skip this result if it doesn't have 7 elements
                            if score > 0.5 and label == 2:  # Label 2 for vehicle detection
                                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
                                cv2.putText(frame, str(id), (int(x1), int(y1) - 10),
                                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

                                # Crop the detected plate
                                cropped_img = frame[int(y1):int(y2), int(x1):int(x2)]
                                plates = lp_detector(cropped_img)
                                
                                for plate in plates[0].boxes.data.tolist():
                                    if plate[4] > 0.6:
                                        px1, py1, px2, py2 = map(int, plate[:4])
                                        cv2.rectangle(cropped_img, (px1, py1), (px2, py2), (255, 0, 0), 2)

                                        # OCR on the cropped license plate
                                        lp_crop = cropped_img[py1:py2, px1:px2]
                                        lp_crop_gray = cv2.cvtColor(lp_crop, cv2.COLOR_BGR2GRAY)
                                        ocr_res = reader.readtext(lp_crop_gray)

                                        min_confidence = 0.3  # You can adjust this threshold as needed

                                        if ocr_res and ocr_res[0][2] > min_confidence:
                                            entry = {'id': id, 'number': ocr_res[0][1], 'score': ocr_res[0][2]}
                                            update_csv(entry)
                                            st.write(f"Detected Plate: {ocr_res[0][1]} (Confidence: {ocr_res[0][2]:.2f})")
                                        else:
                                            st.write("Detected low-confidence plate, skipping...")

                        
                        # Write frame to the output video
                        out.write(frame)

                    frame_nbr += 1

                    # Break if 'q' key is pressed
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break

            # Release resources after processing
            out.release()
            cap.release()
            cv2.destroyAllWindows()

            st.session_state.value_set = False  # Reset session state after processing

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

if not st.session_state.value_set:
    # Provide download links after processing
    st.header("📊 Download Results")
    
    # CSV download button
    st.download_button(label="Download CSV", data="output.csv", file_name="output.csv", key="csv")

    # Video download button
    video_file = open("output_video.mp4", "rb")
    video_bytes = video_file.read()
    video_file.close()
    
    st.download_button(
        label="Download Processed Video",
        data=video_bytes,
        file_name="output_video.mp4",
        mime="video/mp4"
    )

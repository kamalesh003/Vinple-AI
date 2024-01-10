import cv2
import pytesseract
from collections import Counter

# Set the path to the Tesseract executable (update with your path)
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Dell\Downloads\Vinple\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(image):
    try:
        # Use Tesseract to extract text
        extracted_text = pytesseract.image_to_string(image)
        return extracted_text.strip()  # Remove leading/trailing spaces
    except Exception as e:
        print(f"Error during text extraction: {e}")
        return None

def get_most_frequent_text(text_list):
    # Count occurrences of each text
    text_counter = Counter(text_list)
    
    # Get the most common text
    most_common_text = text_counter.most_common(1)

    return most_common_text[0][0] if most_common_text else None

def main():
    try:
        # Capture image using OpenCV
        camera = cv2.VideoCapture(0)  # 0 for default camera

        if not camera.isOpened():
            print("Error: Couldn't open camera.")
            return

        extracted_texts = []  # List to store extracted texts

        while True:
            _, image = camera.read()

            # Extract text from the image
            extracted_text = extract_text_from_image(image)

            if extracted_text:
                extracted_texts.append(extracted_text)

            # Display the captured image
            cv2.imshow('Camera', image)

            # Check for the 'Esc' key to exit the loop
            key = cv2.waitKey(1)
            if key == 27:  # 27 is the ASCII code for 'Esc'
                break

        # Get the most common text from the list
        most_common_text = get_most_frequent_text(extracted_texts)

        if most_common_text:
            print("Most Common Text:", most_common_text)
        else:
            print("No text extracted.")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Release the camera and close all OpenCV windows
        camera.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()


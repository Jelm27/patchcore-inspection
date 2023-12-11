import cv2
import os
import numpy as np

TYPE = "front_large"
SPLIT = "train"
FOLDER = "good"

FOLDER_PATH = f"/Users/jorge/Desktop/Arbeit/IFW/milling_cutter/{TYPE}/{SPLIT}/{FOLDER}"
SAVE_FOLDER_PATH = f"/Users/jorge/Desktop/Arbeit/IFW/milling_cutter/{TYPE}/{SPLIT}/{FOLDER}_cropped"

# Front Small
# MIN_RADIUS = 170
# MAX_RADIUS = 300

# Front Large
MIN_RADIUS = 350
MAX_RADIUS = 450



def detect_circle(img, dp=1.5, min_dist=100, param1=100, param2=30, min_radius=0, max_radius=0):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Apply CLAHE (Contrast Limited Adaptive Histogram Equalization)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    contrast_enhanced = clahe.apply(gray)

    blurred = cv2.GaussianBlur(contrast_enhanced, (9, 9), 2)
    # blurred = cv2.medianBlur(contrast_enhanced, 5)
    # blurred = cv2.GaussianBlur(gray, (9, 9), 2)

    # Change hyperparameters, if necessary, to detect the circle
    circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, dp=1.2, minDist=100, param1=50, param2=30, minRadius=MIN_RADIUS, maxRadius=MAX_RADIUS)
    # gray = cv2.medianBlur(gray, 5)
    # circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp, min_dist, param1=param1, param2=param2, minRadius=min_radius, maxRadius=max_radius)
    
    if circles is not None:
        circles = np.uint16(np.around(circles))
        x, y, r = circles[0][0]
        return (x, y, r)
    return None

def center_circle(img, circle):
    x, y, r = circle
    height, width = img.shape[:2]
    center_x, center_y = width // 2, height // 2

    shift_x, shift_y = center_x - x, center_y - y
    M = np.float32([[1, 0, shift_x], [0, 1, shift_y]])

    centered_img = cv2.warpAffine(img, M, (width, height))
    return centered_img


def crop_circle(img, circle, offset_y=0):
    x, y, r = circle
    height, width = img.shape[:2]

    # Calculate the square bounds
    x1 = max(x, 0)
    y1 = max(y - r - r*offset_y//100, 0)
    x2 = min(x + 2*r, width - 1)
    y2 = min(y + r + r*offset_y//100, height - 1)

    # Crop the image to the square
    square_cropped_img = img[y1:y2, x1:x2]

    return square_cropped_img

if __name__ == "__main__":
    if not os.path.exists(SAVE_FOLDER_PATH):
        os.makedirs(SAVE_FOLDER_PATH)

    for filename in os.listdir(FOLDER_PATH):
        if filename.lower().endswith((".jpg", ".png", ".jpeg")):
            if not os.path.exists(f'{SAVE_FOLDER_PATH}/{filename}'):
                try:
                    image = cv2.imread(f"{FOLDER_PATH}/{filename}")
                    circle = detect_circle(image)
                    if circle:
                        # Center the circle
                        centered_image = center_circle(image, circle)
                        centered_circle = detect_circle(centered_image)

                        # Crop the image to the circle
                        cropped_circle_image = crop_circle(centered_image, centered_circle, 0)

                        # Save the images
                        cv2.imwrite(f'{SAVE_FOLDER_PATH}/{filename}', cropped_circle_image)
                        print(f"Processed and saved: {SAVE_FOLDER_PATH}/{filename}")
                except:
                    print(f"Error processing: {filename}")







# FILE_PATH = "/Users/jorge/Desktop/Arbeit/IFW/milling_cutter/front_small/train/good"
# FILE_NAME = "0291.jpg"
# SAVE_FILE_PATH = "/Users/jorge/Desktop/"


# # Load the image
# image = cv2.imread(f"{FILE_PATH}/{FILE_NAME}")

# # Detect the circle
# circle = detect_circle(image)

# if circle:
#     # Draw the circle on the original image
#     marked_image = image.copy()
#     cv2.circle(marked_image, (circle[0], circle[1]), circle[2], (0, 255, 0), 3)

#     # Center the circle
#     centered_image = center_circle(image, circle)
#     centered_circle = detect_circle(centered_image)

#     # Crop the image to the circle
#     cropped_circle_image = crop_circle(centered_image, centered_circle, 100)

#     # Save the images
#     cv2.imwrite(f'{SAVE_FILE_PATH}/marked_image.jpg', marked_image)
#     cv2.imwrite(f'{SAVE_FILE_PATH}/centered_image.jpg', centered_image)
#     cv2.imwrite(f'{SAVE_FILE_PATH}/cropped_circle_image.jpg', cropped_circle_image)





# if circle:
#     # Center the circle
#     centered_image = center_circle(image, circle)

#     # Display the result
#     cv2.imshow("Centered Circle", centered_image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()


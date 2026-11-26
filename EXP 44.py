
import cv2
import numpy as np

# Read input image
image = cv2.imread("image.jpg")

# Check image
if image is None:
    print("Image not found!")
else:
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding for segmentation
    ret, segmented = cv2.threshold(
        gray, 127, 255, cv2.THRESH_BINARY
    )

    # Display original and segmented images
    cv2.imshow("Original Image", image)
    cv2.imshow("Segmented Image", segmented)

    # Save segmented image
    cv2.imwrite("segmented.jpg", segmented)

    print("Image Segmentation Completed!")

    cv2.waitKey(0)
    cv2.destroyAllWindows()

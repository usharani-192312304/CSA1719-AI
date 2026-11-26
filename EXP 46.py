from ultralytics import YOLO

# Load the pre-trained YOLOv8 model
model = YOLO("yolov8n.pt")

# Input image
image_path = "image.jpg"

# Perform object detection
results = model(image_path)

# Display detected objects
for result in results:
    for box in result.boxes:
        class_id = int(box.cls[0])
        confidence = float(box.conf[0])

        object_name = model.names[class_id]

        print("Object:", object_name)
        print("Confidence:", round(confidence * 100, 2), "%")

    # Display image with detection boxes
    result.show()

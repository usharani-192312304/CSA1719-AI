import face_recognition

# Load known face image
known_image = face_recognition.load_image_file("known.jpg")
known_encoding = face_recognition.face_encodings(known_image)[0]

# Load test image
test_image = face_recognition.load_image_file("test.jpg")
test_encodings = face_recognition.face_encodings(test_image)

# Perform face recognition
for encoding in test_encodings:
    results = face_recognition.compare_faces(
        [known_encoding], encoding
    )

    if results[0]:
        print("Face Recognized: Match Found")
    else:
        print("Face Not Recognized")

import cv2

prototxt = "deploy.prototxt"
model = "res10_300x300_ssd_iter_140000.caffemodel"

# Load model
net = cv2.dnn.readNetFromCaffe(prototxt, model)
cap = cv2.VideoCapture(0)  # Use default webcam

print("🎥 Starting live face blur... Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    (h, w) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0,
                                 (300, 300), (104.0, 177.0, 123.0))
    net.setInput(blob)
    detections = net.forward()

    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.5:
            box = detections[0, 0, i, 3:7] * (w, h, w, h)
            (x1, y1, x2, y2) = box.astype("int")
            face = frame[y1:y2, x1:x2]
            if face.size > 0:
                face = cv2.GaussianBlur(face, (51, 51), 30)
                frame[y1:y2, x1:x2] = face

    cv2.imshow("Live Face Blur", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("✅ Live stream ended.")

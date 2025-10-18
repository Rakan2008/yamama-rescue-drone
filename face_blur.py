import cv2
import os

prototxt = "deploy.prototxt"
model = "res10_300x300_ssd_iter_140000.caffemodel"

# Check model files
if not os.path.exists(prototxt) or not os.path.exists(model):
    print("❌ Model files are missing.")
    exit()

# Load the Caffe face detection model
net = cv2.dnn.readNetFromCaffe(prototxt, model)

# Read input image
image = cv2.imread("example/1.jpg")
if image is None:
    print("❌ Could not open the image.")
    exit()

(h, w) = image.shape[:2]

# Create a blob and pass it through the network
blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0,
                             (300, 300), (104.0, 177.0, 123.0))
net.setInput(blob)
detections = net.forward()

count = 0
for i in range(detections.shape[2]):
    confidence = detections[0, 0, i, 2]
    if confidence > 0.5:
        box = detections[0, 0, i, 3:7] * (w, h, w, h)
        (x1, y1, x2, y2) = box.astype("int")
        face = image[y1:y2, x1:x2]
        if face.size > 0:
            face = cv2.GaussianBlur(face, (51, 51), 30)
            image[y1:y2, x1:x2] = face
            count += 1

print(f"🔍 Detected {count} faces")
cv2.imwrite("example/output.jpg", image)
print("✅ Output saved at example/output.jpg")

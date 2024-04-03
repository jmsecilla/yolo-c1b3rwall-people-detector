from ultralytics import YOLO

# Load a pretrained YOLO model (recommended for training)
model = YOLO('yolov8s.pt')

# Train the model
results = model.train(data='/home/jmcastillo/PycharmProjects/peopleDetector/dataset/data.yaml', epochs=10, imgsz=640, batch=24)

# Evaluate the model's performance on the validation set
results = model.val()

# Export the model to ONNX format
success = model.export(format='onnx')
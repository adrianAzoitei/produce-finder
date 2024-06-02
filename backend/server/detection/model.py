from django.core.files.uploadedfile import InMemoryUploadedFile
import numpy as np
from ultralytics import YOLO
import json

Results = dict[str, dict]

# TODO: use a model factory
class Detector:
    def detect(self, image: np.ndarray, model: str) -> Results:
        detector = YOLO(f"server/detection/models/{model}.pt")
        return json.loads(detector.predict(image, save=False)[0].tojson())
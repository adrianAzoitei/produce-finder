from django.core.files.uploadedfile import InMemoryUploadedFile
import numpy as np
from ultralytics import YOLO
from ultralytics.engine.results import Results

# TODO: use a model factory
class Detector:
    def detect(self, image: np.ndarray, model: str) -> list[Results]:
        detector = YOLO(f"server/detection/{model}.pt")
        return detector.predict(image, save=False)
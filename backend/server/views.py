from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest
from django.core import serializers
from django.views.decorators.http import require_http_methods
import numpy as np
import cv2
import json
from json.decoder import JSONDecodeError
from ultralytics.engine.results import Results
from server.detection.model import Detector

@require_http_methods(["POST"])
def detect(request: HttpRequest, user_id: str) -> HttpResponse:
    detector = Detector()
    if "file" in request.FILES:
        with request.FILES["file"] as f:
            file_bytes = np.asarray(bytearray(f.read()), dtype=np.uint8)
            image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
            results: list[Results] = None
            try:
                if "json" in request.POST:
                    results = detector.detect(image, json.loads(request.POST["json"])["model"])
                else:
                    results = detector.detect(image, "yolov9e")
            except JSONDecodeError:
                return HttpResponseBadRequest(f"could not parse 'json' form field: {request.POST.get('json')}")
            except FileNotFoundError:
                return HttpResponseBadRequest(f"weights for {json.loads(request.POST["json"])["model"]} do not exist")
            except TypeError as e:
                return HttpResponse(e)
            results[0].show()
        return HttpResponse({}, content_type="application/json")
    else:
        return HttpResponseBadRequest("file field missing from form")
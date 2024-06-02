from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest
from django.core import serializers
from django.views.decorators.http import require_http_methods
import numpy as np
import cv2
import json
from json.decoder import JSONDecodeError
from server.detection.model import Detector, Results
from server.models import User, Detection

@require_http_methods(["POST"])
def detect(request: HttpRequest, user_id: str) -> HttpResponse:
    detector = Detector()
    usr = User(user_id)
    usr.save()
    if "file" in request.FILES:
        with request.FILES["file"] as f:
            file_bytes = np.asarray(bytearray(f.read()), dtype=np.uint8)
            image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
            results: Results = None
            try:
                if "json" in request.POST:
                    results = detector.detect(image, json.loads(request.POST["json"])["model"])
                else:
                    results = detector.detect(image, "yolov9e")
            except JSONDecodeError:
                return HttpResponseBadRequest(f"could not parse 'json' form field: {request.POST.get('json')}")
            except FileNotFoundError:
                return HttpResponseBadRequest(f"could not find weights for {json.loads(request.POST["json"])["model"]}")
            except TypeError as e:
                return HttpResponseBadRequest(e)
            d = Detection(user=usr, bboxes=results)
            d.save()
        return HttpResponse(json.dumps(results), content_type="application/json")
    else:
        return HttpResponseBadRequest("file field missing from form")
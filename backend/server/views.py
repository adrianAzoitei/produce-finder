from django.http import HttpRequest, HttpResponse, JsonResponse, HttpResponseBadRequest
from server.models import Produce
from django.core import serializers
from django.views.decorators.http import require_http_methods
from pprint import pprint

@require_http_methods(["POST"])
def detect(request: HttpRequest) -> HttpResponse:
    if "file" in request.FILES:
        with request.FILES["file"] as f:
            print("ok!")
        data = serializers.serialize('json', Produce.objects.filter(pk="2"))
        return HttpResponse(data, content_type="application/json")
    else:
        return HttpResponseBadRequest("file field missing from form")
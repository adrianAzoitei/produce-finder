from django.http import HttpResponse, HttpRequest, HttpResponseBadRequest
from server.models import Produce
from django.views.decorators.http import require_http_methods

@require_http_methods(["POST"])
def detect(request: HttpRequest) -> HttpResponse:
    if "file" in request.FILES:
        with request.FILES["file"] as f:
            print(f.read())
        return HttpResponse()
    else:
        return HttpResponseBadRequest("file field missing from form")
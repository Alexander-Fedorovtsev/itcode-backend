import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.utils import timezone
from .models import Person
from django.shortcuts import get_object_or_404


def index(request):
    now = timezone.now()
    # response = HttpResponse(f'<h1>Hello django!</h1>{now}')
    response = render(request, template_name="core/index.html", context={"dt": now})
    return response


def persons(request):
    object_list = []
    for p in Person.objects.all():
        object_list.append({
            "id": p.id,
            "name": p.name,
        })
    content = json.dumps(object_list)
    response = JsonResponse({"results": object_list}, status=400)
    return response


def person(request, id):
    p = get_object_or_404(Person, id=id)
    detail = {
        "id": id,
        "name": p.name,
        "phone": p.phone,
    }
    return JsonResponse({"results": detail})
# return render(request, "core/index.html")

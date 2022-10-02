import json

from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from .models import Person


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
    return HttpResponse(object_list)

# return render(request, "core/index.html")

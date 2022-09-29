from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone


def index(request):
    now = timezone.now()
    # response = HttpResponse(f'<h1>Hello django!</h1>{now}')
    response = render(request, template_name="core/index.html", context={"dt": now})
    return response

# return render(request, "core/index.html")

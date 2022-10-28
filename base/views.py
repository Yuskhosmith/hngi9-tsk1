from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def endpoints(request):
    data = {
        "slackUsername": "Yuskhosmith",
        "backend": True,
        "age": 20,
        "bio": "I don't know, What do you think?"
    }
    return JsonResponse(data, safe=False)
    
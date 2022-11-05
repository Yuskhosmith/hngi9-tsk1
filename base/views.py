from tkinter import Y
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(["GET"])
def endpoints(request):
    data = {
        "slackUsername": "Yuskhosmith",
        "backend": True,
        "age": 20,
        "bio": "I don't know, What do you think?"
    }
    return Response(data)
@api_view(["GET","POST"])
def post(request):

    data = {
        "slackUsername": "Yuskhosmith",
        "result": "",
        "operation_type": ""
    }

    if request.method == "GET":
        return Response(data)
    else:
        data = request.data
        a = data["operation_type"]
        x = data["x"]
        y = data["y"]
        if "add" in a:
            result = x+y
        elif "subtract" in a:
            result = x-y
        elif "multipl" in a:
            result = x * y
        else:
            result = [x, y]
        r = {
            "slackUsername": "Yuskhosmith",
            "result": result,
            "operation_type": a
            }
        return Response(r)

"""
{"operation_type": "addition" , "x": 1, "y": 2}
Sample Input { "operation_type": Enum <addition | subtraction | multiplication> , "x": Integer, "y": Integer }
Sample Response Format { "slackUsername": String, "result": Integer, "operation_type": Enum.value }
"""
    
from django.shortcuts import render
from django.http import JsonResponse

def get_product(request, productId):
    return JsonResponse({"id": productId, "name": f"{productId} name"})

from django.shortcuts import render
from django.http import JsonResponse

def get_product(request, productId):
    return JsonResponse({"id": productId, "name": f"{productId} name"})

def get_product_list(request):
    products = [
        {"id": "1", "name": "1 name"},
        {"id": "2", "name": "2 name"},
        {"id": "3", "name": "3 name"}
    ]
    return JsonResponse(products, safe=False)
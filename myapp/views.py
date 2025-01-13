from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import Item

def get_items(request):
    items = Item.objects.all().values()  # Retrieve all items
    return JsonResponse(list(items), safe=False)  # Return as JSON

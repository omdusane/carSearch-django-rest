from django.shortcuts import render
from .models import Carlist
from django.http import JsonResponse
from .serializers.car_serializer import CarSerializer
from rest_framework.response import  Response
from rest_framework.decorators import api_view
from rest_framework import status
# import 


# Create your views here.

# def car_list_view(request):
#     car = Carlist.objects.all()
#     data = {
#         'cars': list(car.values()),
#     }
#     return JsonResponse(data)

# def car_detail_view(request, pk):
#     car = Carlist.objects.get(pk=pk)
#     data = { 
#         'name': car.name,
#         'description': car.description,
#         'active': car.active, 
#     }   
#     return JsonResponse(data)

@api_view(['GET', 'POST'])
def car_list_view(request):
    if request.method == 'GET':
        car = Carlist.objects.all()
        serializer = CarSerializer(car, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else: return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def car_detail_view(request, pk):
    if request.method == 'GET':
        try:
            car = Carlist.objects.get(pk=pk)
        except: return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CarSerializer(car)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        car = Carlist.objects.get(pk=pk)
        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        car = Carlist.objects.get(pk=pk)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


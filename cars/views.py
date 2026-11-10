from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Car
from .serializers import CarSerializer
# Create your views here.

@api_view(["GET","POST"])
def car_list(request):
    if request.method == "GET":
        cars = Car.objects.all()
        make = request.query_params.get("make")
        max_price = request.query_params.get("max_price")
        ordering = request.query_params.get("ordering")
        if make:
            cars = cars.filter(make__iexact= make)
        if max_price:
            cars = cars.filter(price__lte = max_price)
        if ordering in ["price", "-price"]:
            cars = cars.order_by(ordering)
        serializer = CarSerializer(cars, many = True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = CarSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= 201)
        else:
            return Response(serializer.errors, status = 400)

@api_view(["GET", "PATCH", "DELETE"])
def car_detail(request, pk):
    if request.method == "GET":
        try:
            car = Car.objects.get(id = pk)
            serializer = CarSerializer(car)
            return Response(serializer.data)
        except Car.DoesNotExist:
            return Response("Car not found" ,status = 404)
    if request.method == "PATCH":
        try:
            car = Car.objects.get(id = pk)
            serializer = CarSerializer(car, data = request.data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = 200)
            else:
                return Response(serializer.errors, status = 400)
        except Car.DoesNotExist:
            return Response("Car not found" ,status = 404)
    if request.method == "DELETE":
        try:
            car = Car.objects.get(id = pk)
            car.delete()
            return Response(status = 204)
        except Car.DoesNotExist:
            return Response("Car not found", status = 404)



    





        


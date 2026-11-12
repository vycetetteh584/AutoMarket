from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Car
from .serializers import CarSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.db.models import Q


class CarPagination(PageNumberPagination):
    page_size =5

# Create your views here.
@api_view(["GET","POST"])
@permission_classes([IsAuthenticatedOrReadOnly])
def car_list(request):
    if request.method == "GET":
        allowed_fields = ["-price", "price", "year", "-year"]
        cars = Car.objects.select_related("seller").all()
        search = request.query_params.get("search")
        min_price = request.query_params.get("min_price")
        max_price = request.query_params.get("max_price")
        make = request.query_params.get("make")
        max_price = request.query_params.get("max_price")
        ordering = request.query_params.get("ordering")
        if make:
            cars = cars.filter(make__iexact= make)
        if max_price:
            try:
                max_price = int(max_price)
                if max_price < 0:
                    return Response({"error": "max_price can't be negative "}, status=400)
                cars = cars.filter(price__lte = max_price)
            except ValueError:
                return Response({"error": "max_price must be a valid number"} ,status = 400)

        if ordering in allowed_fields:
            cars = cars.order_by(ordering, "id")
        else:
            cars = cars.order_by("id")
        if search:
            cars = cars.filter(Q(make__icontains = search) | Q(model__icontains = search))
        paginator = CarPagination()
        if min_price:
            cars = cars.filter(price__gte = min_price)
        if max_price:
            cars = cars.filter(price__lte = max_price)
        page = paginator.paginate_queryset(cars,request)
        serializer = CarSerializer(page, many = True)
        return paginator.get_paginated_response(serializer.data)
    elif request.method == "POST":
        serializer = CarSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save(seller = request.user)
            return Response(serializer.data, status= 201)
        else:
            return Response(serializer.errors, status = 400)

@api_view(["GET", "PATCH", "DELETE"])
@permission_classes([IsAuthenticatedOrReadOnly])
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
            if car.seller != request.user:
                return Response({"error": "You do not own this car"}, status=403)            
            else:
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
            if car.seller != request.user:
                return Response({"error": "You do not own this car"}, status=403)
            else:
                car.delete()
            return Response(status = 204)
        except Car.DoesNotExist:
            return Response("Car not found", status = 404)



    





        


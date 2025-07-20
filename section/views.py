from django.shortcuts import render, get_object_or_404
from .models import Car

def index_view(request):
    cars = Car.objects.all()
    return render(request, 'section/index.html', {'cars': cars})

def car_detail_view(request, pk):
    car = get_object_or_404(Car, pk=pk)
    return render(request, 'section/car_detail.html', {'car': car})

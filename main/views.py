from django.http import Http404
from django.shortcuts import render, get_object_or_404

from main.models import Car
from main.models import Sale
from django.db.models import Q

def cars_list_view(request):
    query = request.GET.get('q')  # извлекаем строку поиска из URL
    if query:
        cars = Car.objects.filter(
            Q(model__icontains=query) |
            Q(color__icontains=query) |
            Q(body_type__icontains=query)
        )
    else:
        cars = Car.objects.all()

    context = {
        'cars': cars,
        'query': query  # чтобы оставить значение в input после поиска
    }

    return render(request, 'main/list.html', context)


def car_details_view(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    context = {
        'car': car
    }
    return render(request, 'main/details.html', context)


def sales_by_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    sales = Sale.objects.filter(car=car)

    context = {
        'car': car,
        'sales': sales
    }

    return render(request, 'main/sales.html', context)

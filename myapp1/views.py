from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from myapp1.models import Vacancy


# Create your views here.

def index_page(request: WSGIRequest) -> render:
    vacancies = Vacancy.objects.all()
    for vac in vacancies:
        print(f"ID = {vac.id}, Фамилия = {vac.second_name}, Имя = {vac.name}, Запрлата = {vac.salary}")

    return render(request, 'index.html')


def about_page(request: WSGIRequest) -> render:
    return render(request, 'about.html')

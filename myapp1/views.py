from django.db.models import QuerySet
from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from rest_framework.viewsets import ModelViewSet

from myapp1.models import Vacancy
from myapp1.serializers import VacancySerializer


# Create your views here.

def index_page(request: WSGIRequest) -> render:
    vacancies = Vacancy.objects.all()
    # for vac in vacancies:
    #     print(f"ID = {vac.id}, Фамилия = {vac.second_name}, Имя = {vac.name}, Запрлата = {vac.salary}")

    return render(request, 'index.html', {"vacancies": vacancies})


def about_page(request: WSGIRequest) -> render:
    return render(request, 'about.html')


class ExampleView(ModelViewSet):
    queryset: QuerySet = Vacancy.objects.all()
    serializer_class = VacancySerializer

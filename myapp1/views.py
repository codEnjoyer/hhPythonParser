# from django.db.models import QuerySet
from django.shortcuts import render, redirect
from django.core.handlers.wsgi import WSGIRequest
from django.db.models import Q
# from rest_framework.viewsets import ModelViewSet

from myapp1.forms import VacancyForm
from myapp1.models import Vacancy


# from myapp1.serializers import VacancySerializer


# Create your views here.

def index_page(request: WSGIRequest) -> render:
    vacancies = Vacancy.objects.filter(Q(name__icontains='python-программист') | Q(name__icontains='пайтон')
                                       | Q(name__icontains='python') | Q(name__icontains='пайтон'))

    return render(request, 'main.html', {'vacancies': vacancies})


def relevance_page(request: WSGIRequest) -> render:
    profession_name = "Python-разработчик"
    header_year = ["Год", "Средняя зарплата", f"Средняя зарплата - {profession_name}", "Количество вакансий",
                   f"Количество вакансий - {profession_name}"]
    # context = {'salary_data': zip(salary_data,
    context = {
        'header_year': header_year,
        'profession_name': f"{profession_name}"}

    return render(request, 'relevance.html', context)


def geography_page(request: WSGIRequest) -> render:
    return render(request, 'geography.html')  # TODO: Написать логику обработки данных


def skills_page(request: WSGIRequest) -> render:
    return render(request, 'skills.html')


def recent_vacancies_page(request: WSGIRequest) -> render:
    return render(request, 'recent_vacancies.html')


def add_vacancy(request: WSGIRequest) -> render:
    error_message = ""
    if request.method == "POST":
        received_form = VacancyForm(request.POST)
        if received_form.is_valid():
            received_form.save()
            return redirect('home')
        else:
            error_message = "Неправильно заполненная форма."

    form = VacancyForm()
    data = {
        'form': form,
        'error_message': error_message
    }
    return render(request, 'add_vacancy.html', data)


def vue_page(request: WSGIRequest) -> render:
    return render(request, "vue.html")

# class ExampleView(ModelViewSet):
#     queryset: QuerySet = Vacancy.objects.all()
#     serializer_class = VacancySerializer

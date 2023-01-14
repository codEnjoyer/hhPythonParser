# from django.db.models import QuerySet
from django.shortcuts import render, redirect
from django.core.handlers.wsgi import WSGIRequest
from django.db.models import Q, Avg, Count, F
# from rest_framework.viewsets import ModelViewSet

from myapp1.forms import VacancyForm
from myapp1.models import Vacancy


# from myapp1.serializers import VacancySerializer


# Create your views here.

def index_page(request: WSGIRequest) -> render:
    return render(request, 'main.html')


def relevance_page(request: WSGIRequest) -> render:
    profession_name = "Python-разработчик"
    header_year = ["Год", "Средняя зарплата", f"Средняя зарплата - {profession_name}", "Количество вакансий",
                   f"Количество вакансий - {profession_name}"]
    prof_filter = Q(name__icontains=f'{profession_name}') | Q(name__icontains='python') | Q(name__icontains='питон')
    prof_count = Count('id', filter=prof_filter)
    prof_salary = Avg('salary', filter=prof_filter)
    statistics_by_years = list(Vacancy.objects
                               .values('published_at')
                               .annotate(total_count=Count('id'), avg_salary=Avg('salary'),
                                         prof_count=prof_count, prof_salary=prof_salary)
                               .values('published_at', 'total_count', 'avg_salary', 'prof_count', 'prof_salary')
                               .order_by())
    data = {
        'header_year': header_year,
        'profession_name': f"{profession_name}",
        'statistics_by_years': statistics_by_years
    }

    return render(request, 'relevance.html', data)


def geography_page(request: WSGIRequest) -> render:
    profession_name = "Python-разработчик"
    header = ["Город", "Всего вакансий", "Средняя зарплата", "Доля вакансий"]

    prof_filter = Q(name__icontains=f'{profession_name}') | Q(name__icontains='python') | Q(name__icontains='питон')
    prof_count = Count('id', filter=prof_filter)
    statistics_by_cities = list(Vacancy.objects
                                .values('area_name')
                                .annotate(total_count=Count('id'),
                                          avg_salary=Avg('salary'),
                                          prof_count=prof_count)
                                .values('area_name', 'total_count', 'avg_salary', 'prof_count')
                                .order_by('-prof_count')[:10]) # TODO: Перевод в проценты
    data = {
        "profession_name": profession_name,
        "header_city": header,
        "statistics_by_cities": statistics_by_cities
    }
    return render(request, 'geography.html', data)


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

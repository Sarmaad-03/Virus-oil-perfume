from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from parfume.models import Parfume
from django.core.paginator import (
                                   Paginator, 
                                   EmptyPage, 
                                   PageNotAnInteger
                                   )


from .models import (
    Bottles,
    MainCarousel,
    WorkPlace,
    WorkerDesc
    ) 
from django.db.models import Q

def index(request):
    all_bottles = Bottles.objects.all()

    
    context = {
        'title': 'Virus Oil Perfume',
        'all_bottles': all_bottles,
    } 

    # Workplace
    try:
        work_img = WorkPlace.objects.all()
        context['work_img'] = work_img
    except:
        print('Something went wrong...while loading workplace img')
    
    # Carousel
    try:  
        carousel = MainCarousel.objects.all()
        context['carousel'] = carousel
    except:
        print('Something went wrong... while loading carousel img')

    # Workers
    try:
        workers = WorkerDesc.objects.all()
        context['workers'] = workers
    except:
        print('Something went wrong...while loading workers img')


    
    return render(request, 'main/landing_page/index.html', context)


def login_employer(request):
    form = AuthenticationForm(request.POST or None)
    if request.user.is_authenticated:
        return redirect('web.home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            return render(request, 'main/landing_page/login.html', 
                  {'form': form, 'title': 'Employer Login'}
                  )
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('web.home')
        else:
            return render(request, 'main/landing_page/login.html', 
                  {'form': form, 'title': 'Employer Login'}
                  )
        
    return render(request, 'main/landing_page/login.html', 
                  {'form': form, 'title': 'Employer Login'}
                  )


def get_page_range(page_obj, max_pages=5):
    """
    Returns a range of page numbers to display, centered around the current page.
    max_pages determines how many page numbers to show at a time.
    """
    start_index = max(page_obj.number - max_pages // 2, 1)
    end_index = min(start_index + max_pages - 1, page_obj.paginator.num_pages)
    
    # Adjust start index if we're at the end of the page list
    if end_index - start_index < max_pages - 1:
        start_index = max(end_index - max_pages + 1, 1)

    return range(start_index, end_index + 1)





def catalog(request):
    # Получаем значения фильтров из запроса GET
    search_query = request.GET.get('search', '')
    filter_category = request.GET.get('category', 'all')  # По умолчанию 'all'

    # Начинаем с получения всех объектов
    parfume_obj = Parfume.objects.all()

    # Применяем фильтрацию по поисковому запросу (если введено)
    if search_query:
        parfume_obj = parfume_obj.filter(
            Q(name__icontains=search_query) | Q(brand__icontains=search_query)
        )

    # Применяем фильтрацию по категории (если выбрана категория и она не "all")
    if filter_category != 'all':
        parfume_obj = parfume_obj.filter(category=filter_category)

    # Пагинация
    paginator_perfume = Paginator(parfume_obj, 10)  # Показывать по 10 товаров на страницу
    page_number_perfume = request.GET.get('page')

    try:
        prod_pag_perfume = paginator_perfume.page(page_number_perfume)
    except PageNotAnInteger:
        prod_pag_perfume = paginator_perfume.page(1)
    except EmptyPage:
        prod_pag_perfume = paginator_perfume.page(paginator_perfume.num_pages)

    # Получаем диапазон страниц для отображения
    perfume_page_range = get_page_range(prod_pag_perfume, max_pages=5)

    context = {
        'parfume_obj': prod_pag_perfume,
        'perfume_page_range': perfume_page_range,
        'title': 'Perfume Catalog',
        'search_query': search_query,
        'filter_category': filter_category,  # Сохраняем выбранную категорию
    }
    
    return render(request, 'main/landing_page/catalog.html', context)





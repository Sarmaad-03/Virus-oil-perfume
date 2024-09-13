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

def catalog(request):
    parfume_obj = Parfume.objects.all()
    
    paginator_perfume = Paginator(parfume_obj, 10)
    page_number_perfume = request.GET.get('page')
    

    try:
        prod_pag_perfume = paginator_perfume.page(page_number_perfume)
    except PageNotAnInteger:
        prod_pag_perfume = paginator_perfume.page(1)
    except EmptyPage:
        prod_pag_perfume =paginator_perfume.page(paginator_perfume.num_pages)
    

    
    context = {
        'parfume_obj': prod_pag_perfume,
        'pag': paginator_perfume,
        'title': 'Perfume Catalog'
    }
    return render(request, 'main/landing_page/catalog.html', context)


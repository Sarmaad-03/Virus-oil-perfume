from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import logout
from customer.models import Gift, Purchase, UserAccount
from parfume.models import Parfume, Parfume_volume

import datetime

from django.core.paginator import (
                                   Paginator, 
                                   EmptyPage, 
                                   PageNotAnInteger
                                   )

from customer.forms import CustomerCreationForm, GiftForm, PurchaseCreationForm




def index(request):
    today = str(datetime.datetime.today()).split(' ')[0].split('-')

    customers_dob = UserAccount.objects.filter(birthday__month=today[1], birthday__day = today[2])
    
    all_purchases = Purchase.objects.all().count()
    all_customers = UserAccount.objects.all()
    all_parfume = Parfume.objects.all()

    paginator_c = Paginator(all_customers, 5)
    page_number_c = request.GET.get('page')

    try:
        prod_pag_customer = paginator_c.page(page_number_c)
    except PageNotAnInteger:
        prod_pag_customer = paginator_c.page(1)
    except EmptyPage:
        prod_pag_customer =paginator_c.page(paginator_c.num_pages)


    context = {
        'title': 'HomePage',
        'all_parfume': all_parfume,
        'all_customers': all_customers,
        'prod_pag_customer': prod_pag_customer,
        'customers_dob': customers_dob,
        'purchases': all_purchases,
    }
    
    return render(request, 'main/employer/index.html', context)


def parfume_list(request):
    all_parfume = Parfume.objects.all()

    paginator = Paginator(all_parfume, 10)
    page_number = request.GET.get('page')

    try:
        prod_pag = paginator.page(page_number)
    except PageNotAnInteger:
        prod_pag = paginator.page(1)
    except EmptyPage:
        prod_pag =paginator.page(paginator.num_pages)


    context = {
        'title': 'Parfumes List',
        'prod_pag': prod_pag,
        'all_parfume': all_parfume,
    } 

    return render(request, 'main/employer/parfume_list.html', context)


def customer_list(request):
    all_customers = UserAccount.objects.all()
    
    paginator = Paginator(all_customers, 10)
    page_number = request.GET.get('page')

    try:
        prod_pag = paginator.page(page_number)
    except PageNotAnInteger:
        prod_pag = paginator.page(1)
    except EmptyPage:
        prod_pag =paginator.page(paginator.num_pages)

    context = {
        'title': 'Customers List',
        'prod_pag': prod_pag,
        'all_customers': all_customers
    }

    return render(request, 'main/employer/customer_list.html', context)


def add_customer(request):
    
    form = CustomerCreationForm(request.POST or None)

    # Adding to DataBase
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Клиент успешно добавлен.'
                )
            return redirect('employer_customer_list')
        
        else:
            messages.warning(
                request, 'Ошибка при добавлении.'
                )

    context = {
        'title': 'Adding Customer',
        'form':form
    }
    return render(request, 'main/employer/add_client.html', context)


def customer_dob(request):
    today = str(datetime.datetime.today()).split(' ')[0].split('-')
    all_customers = UserAccount.objects.filter( birthday__month = today[1], birthday__day = today[2] )

    paginator = Paginator(all_customers, 10)
    page_number = request.GET.get('page')

    try:
        prod_pag = paginator.page(page_number)
    except PageNotAnInteger:
        prod_pag = paginator.page(1)
    except EmptyPage:
        prod_pag =paginator.page(paginator.num_pages)

    context = {
        'title': 'Customer-Birthdays',
        'prod_pag': prod_pag,
        "all_customers": all_customers
    }
    return render(request, 'main/employer/customer_birthdays.html', context) 


def purchases_list(request):
    all_purchases = Purchase.objects.all()

    paginator = Paginator(all_purchases, 10)
    page_number = request.GET.get('page')

    try:
        prod_pag = paginator.page(page_number)
    except PageNotAnInteger:
        prod_pag = paginator.page(1)
    except EmptyPage:
        prod_pag =paginator.page(paginator.num_pages)



    context = {
        'title': 'Purchase List', 
        'all_purchases': all_purchases,
        'prod_pag':prod_pag
    }
    return render(request, 'main/employer/purchase_list.html', context)  


def parfume_volume_list(request,pk):
    parfume = Parfume.objects.get(id=pk)
    context = {
        'parfume': parfume
    }
    return render(request, 'main/employer/parfume_volume_list.html', context)



def make_purchase(request):
    form = PurchaseCreationForm(request.POST or None)


    # adding to db
    if request.method == 'POST':
        if form.is_valid():
            p = request.POST['parfume']
            parfume = Parfume_volume.objects.get(id = p)

            
            form.save()
            messages.success(
                request, 'Сделка успешно добавлена.'
                )
            return redirect('employer_purchasaes')

    context = {
        'title': 'Adding Puurchase',
        'form': form,
    }
    return render(request, 'main/employer/add_purchase.html', context)


def customer_detail(request, id):
    customer = UserAccount.objects.get(id = id)
    context = {
        'title': 'Customers Detail',
        'customer': customer
    }
    return render(request, 'main/employer/customer_detail.html', context)

def gift_list(request):
    gifts = Gift.objects.all()
    num = gifts.count()
    paginator = Paginator(gifts, 10)
    page_number = request.GET.get('page')

    try:
        prod_pag = paginator.page(page_number)
    except PageNotAnInteger:
        prod_pag = paginator.page(1)
    except EmptyPage:
        prod_pag =paginator.page(paginator.num_pages)



    context = {
        'title': 'Gift List',
        'prod_pag': prod_pag,
        'num': num
    }
    return render(request, 'main/employer/gift_list.html', context)

def gift_delete(request, id):
    try:
        obj = Gift.objects.get(id=id)
        obj.delete()
        messages.success(
                    request, 'Успешно удалено.'
                    )
    except:
        
        messages.warning(
                    request, 'Ошибка при удалении.'
                    )
        
    return redirect('employer_gift_list')

def give_gift(request, id):
    client = UserAccount.objects.get(id = id)
    if request.method == 'POST':
        p_id = request.POST.get('parfume')
        p = Parfume_volume.objects.get(id = p_id )
        messages.success(
                    request, 'Успешно добавлено.'
                    )

        Gift.objects.create(
            user=client,
            parfume = p)
        return redirect('employer_customer_list')
    
    form = GiftForm(request.POST or None)
    context = {
        'title':'Adding Gift',
        'form': form,
        'id': id
    }

    return render(request, 'main/employer/add_gift.html', context)



def UserLogout(request):
    logout(request)
    return redirect('web.home')
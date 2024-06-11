# Basic
from django.contrib.auth.models import User
from django.contrib.auth import  logout
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.core.paginator import (
                                   Paginator, 
                                   EmptyPage, 
                                   PageNotAnInteger
                                   )
import datetime
from django.http import HttpResponseRedirect, JsonResponse


# Models
from parfume.models import Parfume, Parfume_volume
from employee.models import Employee
from customer.models import (
                             UserAccount, 
                             Purchase, Gift
                             )

from landing_page.models import (MainCarousel,
                                 Bottles,
                                 WorkPlace,
                                 WorkerDesc
                                )


# Forms
from employee.forms import (UserForm,
                            EmployeeForm
                             )
from parfume.forms import ParfumeForm, ParfumeVolumeForm
from customer.forms import (
                            CustomerCreationForm, 
                            PurchaseCreationForm,
                            GiftForm
                            )

from landing_page.forms import M_CarouselForm, BottlesForm, WorkersForm, WorkPlaceForm
from django.views.decorators.http import require_GET


# Main admin interface

def index(request):
    today = str(datetime.datetime.today()).split(' ')[0].split('-')

    customers_dob = UserAccount.objects.filter(birthday__month=today[1], birthday__day = today[2])
    
    all_purchases = Purchase.objects.all().count()
    all_customers = UserAccount.objects.all()
    all_parfume = Parfume.objects.all()

    
    # For Customer

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
    
    return render(request, 'main/admin/index.html', context)


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
        'menu': 'admin_parfume_list',
        'prod_pag': prod_pag,
        'all_parfume': all_parfume,
    } 

    return render(request, 'main/admin/parfume_list.html', context)



def parfume_volume_list(request,pk):
    parfume = Parfume.objects.get(id=pk)
    context = {
        # 'parfume': parfume,
        'parfume': parfume
    }
    return render(request, 'main/admin/parfume_volume_list.html', context)


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
        'menu': 'admin_customer_list',
        'prod_pag':prod_pag,
        'all_customers': all_customers,
    } 

    return render(request, 'main/admin/customer_list.html', context)

def add_customer(request):
    form = CustomerCreationForm(request.POST or None)

    # Adding to DataBase
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Клиент успешно добавлен.'
                )
            return redirect('admin_customer_list')
        
        else:
            messages.warning(
                request, 'Ошибка при добавлении.'
                )

    context = {
        'title': 'Adding Customer',
        'menu': 'admin_add_customer',
        'form':form
    }
    return render(request, 'main/admin/add_client.html', context)

# Actions with Parfume

def add_parfume(request):
    form = ParfumeForm(request.POST or None)
    

    # Adding to DataBase
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Парфюм успешно добавлен.'
                )
            return redirect('admin_parfume_list')
        
        else:
            messages.warning(
                request, 'Ошибка при добавлении.'
                )

    context = {
        'title': 'Adding Parfume',
        'menu': 'admin_add_parfume',
        'form':form
    }
    return render(request, 'main/admin/add_parfume.html', context)



def delete_parfume(request, id):
    try:
        obj = Parfume.objects.get(id=id)
        obj.delete()
        messages.success(
                    request, 'Парфюм успешно удален.'
                    )
    except:
        
        messages.warning(
                    request, 'Ошибка при удалении.'
                    )
        
    return redirect('admin_parfume_list')


def edit_parfume(request, id):
    obj = get_object_or_404(Parfume, id=id)
    
    
    if request.method == 'GET':
        context = {'form': ParfumeForm(instance=obj), 
                   'title': 'Parfume List',
                   'id': id}
        return render(request, 'main/admin/edit_parfume.html', context)
    
    # Editing Parfume
    elif request.method == 'POST':
        form = ParfumeForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Парфюм успешно изменен.'
                )
            return redirect('admin_parfume_list')
        else:
            messages.warning(
                request, 'Ошибка при изменении.'
                )
            return render(request, 'main/admin/edit_parfume.html', context)
    

def dob_filter(request):
    today = str(datetime.datetime.today()).split(' ')[0].split('-')


    customers = UserAccount.objects.filter(birthday__month=today[1], birthday__day = today[2])

                    

    paginator = Paginator(customers, 10)
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
    }
    return render(request, 'main/admin/customer_birthdays.html', context)   


def customer_detail(request, id):
    customer = UserAccount.objects.get(id = id)
    context = {
        'title': 'Customers Detail',
        'customer': customer
    }
    return render(request, 'main/admin/customer_detail.html', context)


def customer_delete(request, id):
    try:
        obj = UserAccount.objects.get(id=id)
        obj.delete()
        messages.success(
                    request, 'Клиент успешно удален.'
                    )
    except:
        
        messages.warning(
                    request, 'Ошибка при удалении.'
                    )
        
    return redirect('admin_customer_list')



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
    return render(request, 'main/admin/purchase_list.html', context)




def make_purchase(request):
    form = PurchaseCreationForm(request.POST or None)


    # adding to db
    if request.method == 'POST':
        # if form.is_valid():
            # form.save()
        
        c = request.POST.get('customer')
        print(c)
        # p = request.POST.get('parfume')
        # Purchase.objects.create(
        #     user = c,
        #     parfume = p
        # )
        messages.success(
            request, 'Сделка успешно добавлена.'
            )
        return redirect('admin_purchasaes')

    context = {
        'title': 'Adding Purchase',
        'form': form,

    }
    return render(request, 'main/admin/add_purchase.html', context)


def delete_purchase(request, id):
    try:
        obj = Purchase.objects.get(id=id)
        obj.delete()
        messages.success(
                    request, 'Сделка успешно удалена.'
                    )
    except:
        
        messages.warning(
                    request, 'Ошибка при удалении.'
                    )
        
    return redirect('admin_purchasaes')
    
# Employers

def add_employee(request):
    
    form = UserForm()
    form_2 = EmployeeForm()

    if request.method == 'POST':
        form = UserForm(request.POST)
        form_2 = EmployeeForm(request.POST) 

        if form.is_valid() and form_2.is_valid():
            user = form.save()
            emp = form_2.save(commit=False)
            emp.user = user
            emp.save()
            
        
            messages.success(
                request, 'Работник успешно добавлен.'
            )
            return redirect('admin_home')
        
        else:
            messages.warning(
                request, 'Что-то пошло не так, проверьте, все ли правильно вы заполнили.'
            )
    context = {
        'title': 'Adding Employee',
        'form': form,
        'form_2': form_2
    }
    return render(request, 'main/admin/add_employee.html', context)

def empployers_list(request):

    all_employers = Employee.objects.all()

    paginator = Paginator(all_employers, 10)
    page_number = request.GET.get('page')

    try:
        prod_pag = paginator.page(page_number)
    except PageNotAnInteger:
        prod_pag = paginator.page(1)
    except EmptyPage:
        prod_pag =paginator.page(paginator.num_pages)

    context = {
        'title': 'Employers List', 
        'all_employers': all_employers,
        'prod_pag':prod_pag
    }
    return render(request, 'main/admin/employers_list.html', context)


def employers_dob(request):
    today = str(datetime.datetime.today()).split(' ')[0].split('-')


    
    emp = Employee.objects.filter(bithday__month = today[1], bithday__day = today[2])

    

    paginator = Paginator(emp, 10)
    page_number = request.GET.get('page')

    try:
        prod_pag = paginator.page(page_number)
    except PageNotAnInteger:
        prod_pag = paginator.page(1)
    except EmptyPage:
        prod_pag =paginator.page(paginator.num_pages)

    context = {
        'title': 'Employee-Birthdays', 
        'prod_pag':prod_pag,
    }
    return render(request, 'main/admin/employers_dob.html', context)


def employer_delete(request, id):
    try:
        obj = Employee.objects.get(id=id)
        user = User.objects.get(id = obj.user.id)
        user.delete()
        obj.delete()
        messages.success(
                    request, 'Работник успешно удален.'
                    )
    except:
        
        messages.warning(
                    request, 'Ошибка при удалении.'
                    )
        
    return redirect('admin_employers_list')

def edit_volume(request, id):

    context = {}

    obj = get_object_or_404(Parfume_volume, id=id)
    
    
    if request.method == 'GET':

        context['form'] = ParfumeVolumeForm(instance=obj)
        context['title'] = 'Editing Volume'
        context['id'] = id

        return render(request, 'main/admin/volume_edit.html', context)
    
    # Editing Volume
    elif request.method == 'POST':
        form = ParfumeVolumeForm(request.POST, instance=obj)
        
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Вариация успешно изменена.'
                )
            return redirect('admin_parfume_list')
        else:
            messages.warning(
                request, 'Ошибка при изменении.'
                )
            
            return redirect('admin_parfume_list')

def delete_volume(request, id):
    try:
        obj = Parfume_volume.objects.get(id=id)
        obj.delete()
        messages.success(
                    request, 'Успешно удалено.'
                    )
    except:
        
        messages.warning(
                    request, 'Ошибка при удалении.'
                    )
        
    return redirect('admin_parfume_list')


def add_volume(request, id):
    
    p = Parfume.objects.get(id=id)
    # Adding to DataBase
    if request.method == 'POST':
        vol = request.POST.get('volum_ml')
        price = request.POST.get('price')


        Parfume_volume.objects.create(
            parfum = p,
            volum_ml = vol,
            price = price
        )
        
            
        messages.success(
            request, 'Вариация успешно добавлена.'
            )
        return redirect('admin_parfume_list')
        
    
    context = {
        'title': 'Adding Volume',
    }
    return render(request, 'main/admin/add_volume.html', context)

def landing_page(request):

    main_carousel = MainCarousel.objects.all()
    bottles = Bottles.objects.all()
    workers = WorkerDesc.objects.all()
    work_places = WorkPlace.objects.all()

    context = {
        'title': 'Edit Page', 
        'main_carousel': main_carousel,
        'bottles':bottles,
        'workers': workers,
        'work_places': work_places,
    }

    return render(request, 'main/admin/editor.html', context)


def delete_m_carousel(request, id):
    try:
        obj = MainCarousel.objects.get(id=id)
        obj.delete()
        messages.success(
                    request, 'Успешно удалено.'
                    )
    except:
        
        messages.warning(
                    request, 'Ошибка при удалении.'
                    )
        
    return redirect('admin_edit_page')

def add_m_carousel(request):
    form = M_CarouselForm(request.POST or None)
    if request.method == 'POST':
        form = M_CarouselForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                    request, 'Успешно добавлено.'
                    )
            return redirect('admin_edit_page')

    context = {
        'title': 'Adding Photo',
        'form': form,
        }
    
    return render(request, 'main/admin/add_m_car.html', context)


def add_bottles(request):
    form = BottlesForm(request.POST or None)
    if request.method == 'POST':
        form = BottlesForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                    request, 'Успешно добавлено.'
                    )
            return redirect('admin_edit_page')

    context = {
        'title': 'Adding Bottle',
        'form': form,
        }
    
    return render(request, 'main/admin/add_bottle.html', context)

def add_work_pht(request):
    form = WorkersForm(request.POST or None)
    if request.method == 'POST':
        form = WorkersForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                    request, 'Успешно добавлено.'
                    )
            return redirect('admin_edit_page')

    context = {
        'title': 'Adding Worker Photo',
        'form': form,
        }
    
    return render(request, 'main/admin/add_work_pht.html', context)

def add_work_place(request):
    form = WorkPlaceForm(request.POST or None)
    if request.method == 'POST':
        form = WorkPlaceForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                    request, 'Успешно добавлено.'
                    )
            return redirect('admin_edit_page')

    context = {
        'title': 'Adding Workplace Photo',
        'form': form,
        }
    
    return render(request, 'main/admin/add_work_place.html', context)


def delete_bottles(request, id):
    try:
        obj = Bottles.objects.get(id=id)
        obj.delete()
        messages.success(
                    request, 'Успешно удалено.'
                    )
    except:
        
        messages.warning(
                    request, 'Ошибка при удалении.'
                    )
        
    return redirect('admin_edit_page')


def delete_work_pht(request, id):
    try:
        obj = WorkerDesc.objects.get(id=id)
        obj.delete()
        messages.success(
                    request, 'Успешно удалено.'
                    )
    except:
        
        messages.warning(
                    request, 'Ошибка при удалении.'
                    )
        
    return redirect('admin_edit_page')

def delete_work_place(request, id):
    try:
        obj = WorkPlace.objects.get(id=id)
        obj.delete()
        messages.success(
                    request, 'Успешно удалено.'
                    )
    except:
        
        messages.warning(
                    request, 'Ошибка при удалении.'
                    )
        
    return redirect('admin_edit_page')


def give_gift(request, id):
    client = UserAccount.objects.get(id = id)
    if request.method == 'POST':
        p_id = request.POST.get('parfume')
        p = Parfume_volume.objects.get(id = p_id )

        Gift.objects.create(
            user=client,
            parfume = p)
        return redirect('admin_customer_list')
    
    form = GiftForm(request.POST or None)
    context = {
        'title':'Adding Gift',
        'form': form,
        'id': id
    }

    return render(request, 'main/admin/add_gift.html', context)


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
    return render(request, 'main/admin/gift_list.html', context)


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
        
    return redirect('admin_gift_list')







@require_GET
def get_items_user(request):
    query = request.GET.get('query', '')
    users = UserAccount.objects.filter(first_name__icontains=query) | UserAccount.objects.filter(last_name__icontains=query)
    
    
    data = [{'id': user.id, 'username': user.first_name, 
             'surname':user.last_name, 'dob':user.birthday, 'purchases': user.quantity() } for user in users]
    return JsonResponse(data, safe=False)

@require_GET
def get_items_parfume(request):
    query = request.GET.get('query', '')
    perfumes = Parfume_volume.objects.filter(parfum__name__icontains=query) | Parfume_volume.objects.filter(parfum__brand__icontains=query) 
    data = [{'id': perfume.id, 'name': perfume.parfum.name, 'brand': perfume.parfum.brand, 
             'ml':perfume.volum_ml, 'price':perfume.price} for perfume in perfumes]
    return JsonResponse(data, safe=False)



def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'




def add_purchase(request):
    data = {}
    if is_ajax(request=request):

        user_id = request.POST.get('user')
        perfume_id = request.POST.get('parfume')

        print(user_id)
        print(perfume_id)
        
        try:
            user = UserAccount.objects.get(id=user_id)
            perfume = Parfume_volume.objects.get(id=perfume_id)
        except:
            print('user not found')
        
        
        purchase = Purchase(user=user, parfume=perfume).save()
        data['status'] = 'ok'
        return JsonResponse(data)
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))



def UserLogout(request):
    logout(request)
    return redirect('web.home')
from django.urls import path
from .views import *


urlpatterns = [
    # main
    path('admin_page/', index, name='admin_home'),
    path('admin_parfume_list/', parfume_list, name='admin_parfume_list'),
    path('admin_parfume_volume_list/<str:pk>/', parfume_volume_list, name='admin_parfume_volume_list'),
    path('admin_customer_list/', customer_list, name='admin_customer_list'),
    path('admin_logout/', UserLogout, name='admin.logout'),

    # actions with parfume
    path('admin_add_parfume/', add_parfume, name='admin_add_parfume'),
    path('admin_delete_parfume/<str:id>/', delete_parfume, name='admin_delete_parfume'),
    path('admin_edit_parfume/<str:id>/', edit_parfume, name='admin_edit_parfume'),
    path('admin_edit_parfume_volume/<str:id>/', edit_volume, name='admin_edit_volume'),
    path('admin_add_parfume_volume/<str:id>/', add_volume, name='admin_add_volume'),
    path('admin_delete_parfume_volume/<str:id>/', delete_volume, name='admin_delete_volume'),
    
    # acions with customer
    path('admin_bd_customers/', dob_filter, name='admin_bd_customers'),
    path('admin_customer_detail/<str:id>/', customer_detail, name='admin_customer_detail'),
    path('admin_customer_delete/<str:id>/', customer_delete, name='admin_customer_delete'),
    path('admin_add_customer/', add_customer, name='admin_add_customer'),

    # actions with purchase
    path('admin_purchase_list/', purchases_list, name='admin_purchasaes'),
    path('admin_make_purchase/', make_purchase, name='admin_make_purchase'),
    path('admin_purchase_delete/<str:id>/', delete_purchase, name='admin_purchase_delete'),
    
    # Employees
    path('admin_add_employee/', add_employee, name='admin_add_employee'),
    path('admin_employer_list/', empployers_list, name='admin_employers_list'),
    path('admin_employer_dob/', employers_dob, name='admin_employers_dob'),
    path('admin_employer_delete/<str:id>/', employer_delete, name='admin_employer_delete'),

    # Gift
    path('admin_give_gift/<str:id>/', give_gift, name='admin_give_gift'),
    path('admin_gift_list/', gift_list, name='admin_gift_list'),
    path('admin_gift_delete/<str:id>/', gift_delete, name='admin_gift_delete'),
    
    # Landing-Page Editor
    path('admin_edit_landing_page/', landing_page, name='admin_edit_page'),

    # 1 Main_carousel
    path('admin_m_carousel_delete/<int:id>/', delete_m_carousel, name='admin_m_carousel_delete'),
    path('admin_add_m_carousel/', add_m_carousel, name='admin_add_m_carousel'),

    # 2 Bottles
    path('admin_bottles_delete/<int:id>/', delete_bottles, name='admin_bottles_delete'),
    path('admin_add_bottles/', add_bottles, name='admin_add_bottles'),

    # 3 Workers
    path('admin_work_pht_delete/<int:id>/', delete_work_pht, name='admin_work_pht_delete'),
    path('admin_add_work_pht/', add_work_pht, name='admin_add_work_pht'),

    # 4 Work-place
    path('admin_delete_work_place/<int:id>/', delete_work_place, name='admin_delete_work_place'),
    path('admin_add_work_place/', add_work_place, name='admin_add_work_place'),
    
    #
    # path('get_items/', get_items, name='get_items'),
    path('add_purchase/', add_purchase, name='add_purchase'),
    path('get_items_user/', get_items_user, name='get_items_user'),
    path('get_items_parfume/', get_items_parfume, name='get_items_parfume'),
    

]

    
    




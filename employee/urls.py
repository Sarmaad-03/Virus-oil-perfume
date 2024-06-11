from django.urls import path
from .views import *

urlpatterns = [
    path('employers_page/', index, name='employer_home'),
    path('employers_parfume_list/', parfume_list, name='employer_parfume_list'),
    path('employers_parfume_volume_list/<str:pk>/', parfume_volume_list, name='employer_parfume_volume_list'),
    path('employers_customer_list/', customer_list, name='employer_customer_list'),
    path('employers_add_customer/', add_customer, name='employer_add_customer'),
    path('employers_customer_dob/', customer_dob, name='employer_customer_dob'),
    path('employers_purchase_list/', purchases_list, name='employer_purchasaes'),
    path('employers_make_purchase/', make_purchase, name='employer_make_purchase'),
    path('employers_customer_detail/<str:id>/', customer_detail, name='employer_customer_detail'),
    path('employers_logout/', UserLogout, name='employer_logout'),
    # gift
    path('employers_gift_list/', gift_list, name='employer_gift_list'),
    path('employers_give_gift/<str:id>/', give_gift, name='employer_give_gift'),
    path('employers_gift_delete/<str:id>/', gift_delete, name='employer_gift_delete'),
]

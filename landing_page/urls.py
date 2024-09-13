from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    # path('', cache_page(60 * 1)(index), name='web.home', ), # 3 min cache
    path('', index, name='web.home', ), # 3 min cache
    path('login/', login_employer, name='web.login'),
    path('catalog/', cache_page(60 * 0)(catalog), name='web.catalog'), # 3 min cache
]

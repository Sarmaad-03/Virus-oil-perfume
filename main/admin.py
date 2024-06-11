from django.contrib import admin
from customer.models import UserAccount
from parfume.models import Parfume, Parfume_volume
from customer.models import Purchase, Gift
from employee.models import Employee
from landing_page.models import (
    WorkerDesc,
    WorkPlace,
    MainCarousel,
    Bottles
)



admin.site.register(UserAccount)
admin.site.register(Parfume)
admin.site.register(Purchase)
admin.site.register(Employee)
admin.site.register(WorkPlace)
admin.site.register(WorkerDesc)
admin.site.register(MainCarousel)
admin.site.register(Bottles)
admin.site.register(Parfume_volume)
admin.site.register(Gift)


from django.db import models
import uuid

from django.urls import reverse


selection = (
    ('Есть','Есть'),
    ('Нет','Нет'),

)

cat_selection =  (
    ('Мужской','Мужской'),
    ('Женский','Женский'),
    ('Унисекс','Унисекс'),
)


class Parfume(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, null = True, blank=True)
    brand = models.CharField(max_length=200)
    toilet_water = models.CharField(max_length=20, choices=selection, null=True, blank=True)
    added_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=250, choices=cat_selection)




    def __str__(self):
        return f"'{self.name}' -  by {self.brand}"
        
    
    def get_absolute_url(self):
        return reverse("#", kwargs={"pk": self.id})
    
    class Meta:
        ordering = ["brand"]
    

class Parfume_volume(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    parfum = models.ForeignKey(Parfume, on_delete = models.CASCADE, related_name = "volumes")
    volum_ml = models.PositiveIntegerField(null=True, blank=True)
    price = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.parfum.name} by {self.parfum.brand}  - {self.volum_ml} Ml" 
    



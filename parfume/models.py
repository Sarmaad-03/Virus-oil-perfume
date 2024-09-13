from django.db import models
import uuid
from django.urls import reverse
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

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
    img = models.ImageField(upload_to='perfume_images/', null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.img and hasattr(self.img, 'file'):
            im = Image.open(self.img)
            max_size = (800, 800)
            im.thumbnail(max_size)

            im_io = BytesIO()
            im.save(im_io, format='WEBP', quality=75)
            new_image = InMemoryUploadedFile(
                im_io, 'ImageField', f'{self.img.name.split(".")[0]}.webp', 
                'image/webp', sys.getsizeof(im_io), None
            )

            self.img = new_image
        super(Parfume, self).save(*args, **kwargs)


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
    



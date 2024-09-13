from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

class MainCarousel(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='carousel_images/',)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
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
        super(MainCarousel, self).save(*args, **kwargs)




class Bottles(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100, null = True, blank = True)
    img = models.ImageField(upload_to='bottle_images/',)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

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
        super(Bottles, self).save(*args, **kwargs)
        
    




class WorkPlace(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=150)
    img = models.ImageField(upload_to='work_images/',)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

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
        super(WorkPlace, self).save(*args, **kwargs)






class WorkerDesc(models.Model):
    name = models.CharField(max_length = 100)
    spec = models.CharField(max_length = 100)
    img = models.ImageField(upload_to='employ_images/',)
    desc = models.CharField(max_length = 100, null = True, blank = True)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
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
        super(WorkerDesc, self).save(*args, **kwargs)

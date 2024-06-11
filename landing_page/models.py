from django.db import models

class MainCarousel(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='carousel_images/',)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Bottles(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100, null = True, blank = True)
    img = models.ImageField(upload_to='bottle_images/',)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class WorkPlace(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=150)
    img = models.ImageField(upload_to='work_images/',)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class WorkerDesc(models.Model):
    name = models.CharField(max_length = 100)
    spec = models.CharField(max_length = 100)
    img = models.ImageField(upload_to='employ_images/',)
    desc = models.CharField(max_length = 100, null = True, blank = True)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

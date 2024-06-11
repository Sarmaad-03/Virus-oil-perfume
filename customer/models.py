from django.db import models
from parfume.models import Parfume, Parfume_volume
import uuid


class UserAccount(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    number = models.IntegerField(null = True, blank = True)
    birthday = models.DateField(null = True, blank = True)


    def __str__(self): 
        return f'{self.first_name} {self.last_name} | {self.birthday} |'
    

    def bought(self):
        total = 0
        for i in self.purchases.all():
            
            total += i.parfume.price
        return total
    
    def quantity(self):
        total = 0
        for i in self.purchases.all():
            
            total += 1
        return total

    


class Purchase(models.Model): 
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(UserAccount, related_name='purchases', on_delete=models.CASCADE)
    parfume = models.ForeignKey(Parfume_volume, related_name='purchases', on_delete=models.CASCADE, null = True, blank = True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.first_name}  at {self.created_at}"
    
    class Meta:
        ordering = ["-created_at"]


    
class Gift(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(UserAccount, related_name='gifts', on_delete=models.CASCADE)
    parfume = models.ForeignKey(Parfume_volume, related_name='gifts', 
                                on_delete=models.CASCADE, null = True, blank = True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.first_name}  at {self.created_at}"
    
    class Meta:
        ordering = ["-created_at"]


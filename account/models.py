from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    birth_data = models.DateField(blank=True,null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d',blank=True)
    username = models.CharField(max_length=30,blank=True,null=True)
    first_name= models.CharField(max_length=30,blank=True,null=True)
    last_name = models.CharField(max_length=30,blank=True,null=True)
    email = models.EmailField(blank=True,null=True)

    def __str__(self):
        return f'profile of {self.user.username}'
    


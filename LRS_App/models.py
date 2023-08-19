from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.

class Contact(models.Model):
    Name = models.CharField(max_length=50)
    Mail = models.EmailField()
    Address = models.CharField(max_length=250)
    Message = models.CharField(max_length=1500)


class UploadedFile(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField()
    filetype = models.CharField(max_length=10,null=True)
    top_resource = models.CharField(max_length=3,null=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_datetime = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.title
    
class UserProfile(models.Model):
   user = models.OneToOneField(User,on_delete=callable)
   plan = models.CharField(
        max_length=10, choices=(('standard', ('Standard')),('business', ('Business')),('premium', ('Premium')),('vip', ('VIP')) ),
        blank=True, null=True)




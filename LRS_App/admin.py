from django.contrib import admin
from .models import Contact,UploadedFile,UserProfile

# Register your models here.

admin.site.register(Contact)
admin.site.register(UploadedFile)
admin.site.register(UserProfile)
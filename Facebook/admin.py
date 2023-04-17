from django.contrib import admin
from .models import Facebook_Data

# Register your models here.

@admin.register(Facebook_Data)
class Facebook_Data_Admin(admin.ModelAdmin):
    list_display=['id','facebook_username','facebook_passsword']


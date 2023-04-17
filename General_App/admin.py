from django.contrib import admin
from .models import CompanyType,Category,Plan,Services,Role,BusinessAccount,User,User_Login

# Register your models here.

@admin.register(CompanyType)
class CompanyType_Admin(admin.ModelAdmin):
    list_display=['id','type_name']

@admin.register(Category)
class Category_Admin(admin.ModelAdmin):
    list_display=['id','company_type']

@admin.register(Plan)
class Plan_Admin(admin.ModelAdmin):
    list_display=['id','plan_name']

@admin.register(Services)
class Services_Admin(admin.ModelAdmin):
    list_display=['id','service_plan_name','service_name']

@admin.register(Role)
class Role_Admin(admin.ModelAdmin):
    list_display=['id','role_name']

@admin.register(BusinessAccount)
class BusinessAccount_Admin(admin.ModelAdmin):
    list_display=['id','company_name','company_type','category','company_website','comapny_plan','company_email','password','mobile_number']

@admin.register(User)
class User_Admin(admin.ModelAdmin):
    list_display=['id','username','user_email','user_mobile','user_role']

@admin.register(User_Login)
class User_Login_Admin(admin.ModelAdmin):
    list_display=['id','user_name','user_role']


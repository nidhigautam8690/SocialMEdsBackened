from django.db import models

# Create your models here.
class CompanyType(models.Model):
    type_name=models.CharField(max_length=50)
    def __str__(self):
        return self.type_name


class Category(models.Model):
    company_type=models.ForeignKey(to=CompanyType, on_delete=models.CASCADE)
    category_name=models.CharField(max_length=50)
    def __str__(self):
        return self.category_name


class Plan(models.Model):
    plan_name=models.CharField(max_length=50)
    def __str__(self):
        return self.plan_name


class Services(models.Model):
    service_plan_name=models.ForeignKey(to=Plan, on_delete=models.CASCADE)
    service_name=models.CharField(max_length=50)
    def __str__(self):
        return self.service_name

class Role(models.Model):
    role_name=models.CharField(max_length=50)
    def __str__(self):
        return self.role_name


class BusinessAccount(models.Model):
    company_name=models.CharField(max_length=50)
    company_type=models.ForeignKey(to=CompanyType, on_delete=models.CASCADE)
    category=models.ForeignKey(to=Category, on_delete=models.CASCADE)
    company_website=models.CharField(max_length=50)
    comapny_plan=models.ForeignKey(to=Plan, on_delete=models.CASCADE)
    company_email=models.EmailField()
    password=models.CharField(max_length=50)
    mobile_number=models.IntegerField(max_length=30)
    def __str__(self):
        return self.company_name


class User(models.Model):
    username=models.CharField(max_length=50)
    user_email=models.CharField(max_length=50)
    user_mobile=models.IntegerField(max_length=30)
    user_role=models.ForeignKey(to=Role, on_delete=models.CASCADE)
    def __str__(self):
        return self.username

class User_Login(models.Model):
    user_name=models.CharField(max_length=50)
    user_password=models.CharField(max_length=50)
    user_role=models.ForeignKey(to=Role, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_name



from django.db import models

# Create your models here.
class Facebook_Data(models.Model):
    facebook_username=models.CharField(max_length=50)
    facebook_passsword=models.CharField(max_length=50)
    def __str__(self):
        return self.facebook_username
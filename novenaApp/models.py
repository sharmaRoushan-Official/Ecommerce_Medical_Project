from django.db import models

# Create your models here.


class contactModel(models.Model):
    name=models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=254,unique=True,blank=False,null=False)
    subject = models.CharField(max_length=100,blank=False, null=False)
    phoneNo = models.CharField(max_length=12,blank=False,null=False)
    message = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.name




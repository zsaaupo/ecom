from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):

    user = models.OneToOneField(User, on_delete=models.PROTECT)
    full_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=11)

    def __str__(self):
        return self.full_name+" "+"("+self.phone_number+")"
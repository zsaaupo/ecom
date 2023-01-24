from django.db import models

class Customer(models.Model):

    full_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=11)

    def __str__(self):
        return self.full_name+" "+"("+self.phone_number+")"

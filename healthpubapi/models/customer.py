from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    DOB = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # @property
    # def full_name(self):
    #     return f'{self.user.first_name} {self.user.last_name}'
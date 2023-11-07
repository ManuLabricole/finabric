from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100, null=False, blank=False)
    lastname = models.CharField(max_length=100, null=False, blank=False)
    birth_date = models.DateField(null=True, blank=True)
    email = models.EmailField(max_length=100, null=False, blank=False, unique=True)
    
    monthly_income = models.IntegerField(null=True, blank=True)
    monthly_expenses = models.IntegerField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.user.username

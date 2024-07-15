from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cargo = models.CharField(max_length=12, choices=(("ADM", 'admin'), ('FUNC','funcionario')))
    



    def __str__(self):
        return self.username
    
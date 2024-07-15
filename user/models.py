from django.db import models


class User(models.Model):
    email = models.EmailField(max_length=250, blank=False, null=False, primary_key=True)
    username=models.CharField(max_length=250, blank=False, null=False)
    password = models.CharField(max_length=250, blank=False, null=False)
    register_date = models.DateTimeField(auto_now_add=True, editable=False)


    def __str__(self):
        return self.username
    
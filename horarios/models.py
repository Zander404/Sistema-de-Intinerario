from django.db import models


class Rote(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250, unique=True, blank=False, null=False)
    box = models.IntegerField(blank=True, null=True)
    weekly_time = models.JSONField()
    sartuday_time = models.JSONField()
    alternative_time = models.JSONField()
    rote = models.URLField(blank=True, help_text='Insira o link da rota google maps para usar renderizar o mapa')


    def __str__(self):
        return self.name
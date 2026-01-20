from django.db import models

class Motocycles(models.Model):
    name = models.CharField(max_length=100)
    body = models.CharField(max_length=100)
    motor = models.FloatField()
    starter = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Motocycles"

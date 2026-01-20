from django.db import models

class Atvs(models.Model):
    name = models.CharField(max_length=100)
    body = models.CharField(max_length=100)
    motor = models.FloatField()
    starter = models.BooleanField(default=False)
    image = models.ImageField(upload_to='atvs/', null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Atvs"

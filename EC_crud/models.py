from django.db import models

# Create your models here.

class BMImodel(models.Model):
    Fullname= models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    height = models.FloatField()
    weight = models.FloatField()
    bmi = models.FloatField(default=1)
    dt= models.DateField(auto_now_add=True)

    def __str__(self):
        return self.Fullname 
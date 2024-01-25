from django.db import models

# Create your models here.

class HeartDisease(models.Model):
    name = models.CharField(max_length =255 , verbose_name='Name')
    age = models.FloatField(verbose_name='Age')
    sex = models.FloatField(verbose_name='Sex')
    cp = models.FloatField(verbose_name='CP')
    trestbps = models.FloatField(verbose_name='TRESTBPS')
    chol = models.FloatField(verbose_name='CHOL')
    fbs = models.FloatField(verbose_name='FBS')  
    restecg = models.FloatField(verbose_name='RESTECG')
    thalach = models.FloatField(verbose_name='THALACH')
    exang = models.FloatField(verbose_name='EXANG')
    oldpeak = models.FloatField(verbose_name='OLDPEAK')
    slope = models.FloatField(verbose_name='SLOPE')
    ca = models.FloatField(verbose_name='CA')
    thal = models.FloatField(verbose_name='THAL')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Date_Time')
    predicted_value = models.CharField(max_length=225, verbose_name= 'predicted_value' ,null=True, blank =True)

    def __str__(self):
        return f"Heart Disease Prediction - {self.id}"
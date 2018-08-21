from django.db import models


# Create your models here.

class Todo (models.Model):
    title = models.CharField(max_length=50 , verbose_name= 'Başlık')
    completed = models.BooleanField(verbose_name='Durum')

    def __str__(self):
        return self.title






class Kitaps (models.Model):
    kitapAdi = models.CharField(verbose_name="Kitaplar" , max_length=150)
    yaazarAdi = models.CharField(verbose_name="Yazarlar" , max_length=150)
    yayineviAdi = models.CharField(verbose_name="YayınEvleri" , max_length=150)
    def __str__(self):
        return "%s %s %s" % (self.kitapAdi , self.yaazarAdi , self.yayineviAdi)


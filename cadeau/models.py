from django.db import models

# Create your models here.
class Artikel(models.Model):
    naam = models.CharField(max_length=1024)
    foto = models.ImageField(blank=True)
    beschrijving = models.TextField()
    beschikbaar_procent = models.IntegerField(default=100, verbose_name="% nog te koop")
    totaal = models.DecimalField(decimal_places=2, max_digits=7, default=0.00)


class Cadeau(models.Model):
    schenker = models.CharField(max_length=1024)
    email_schenker = models.EmailField()

    totaal = models.DecimalField(decimal_places=2, max_digits=7)
    betaald = models.BooleanField(default=False)

    cadeauItems = models.ManyToManyField(Artikel, through="CadeauItem")

class CadeauItem(models.Model):
    artikel = models.ForeignKey(Artikel)
    cadeau = models.ForeignKey(Cadeau)

    percent = models.IntegerField()
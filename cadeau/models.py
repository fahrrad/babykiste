from django.db import models

# Create your models here.
class Artikel(models.Model):
    naam = models.CharField(max_length=1024)
    foto = models.ImageField(blank=True)
    beschrijving = models.TextField()
    beschikbaar_procent = models.IntegerField(default=100, verbose_name="% nog te koop")
    totaal = models.DecimalField(decimal_places=2, max_digits=7, default=0.00)

    def image_tag(self):
        return u'<img src="%s" />' % self.foto.url

    image_tag.short_description = "Foto"
    image_tag.allow_tags = True

    def percent(self):
        return 100 - self.beschikbaar_procent
    percent.short_description = "percent gegeven"

    def __str__(self):
        return self.naam


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
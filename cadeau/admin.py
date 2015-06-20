from django.contrib import admin

# Register your models here.
from django.contrib.admin import register
from cadeau.models import Artikel


@register(Artikel)
class ArtikelAdmin(admin.ModelAdmin):
    readonly_fields = ('image_tag', 'percent')

    pass
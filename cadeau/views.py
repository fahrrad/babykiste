from django.shortcuts import render




# Create your views here.
from cadeau.models import Artikel


def bevestig(request):
    if request.method == 'GET':
        bestel_form = None
        return render(request, 'bevestig.html', {'form': bestel_form})


def lijst(request):
    return render(request, 'lijst.html', {'artikels': Artikel.objects.all()})


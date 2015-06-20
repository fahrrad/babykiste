from django.shortcuts import render




# Create your views here.
def bevestig(request):
    if request.method == 'GET':
        bestel_form = None
        return render(request, 'bevestig.html', {'form': bestel_form})


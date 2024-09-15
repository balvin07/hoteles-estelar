from django.shortcuts import render, redirect
from .forms import EncuestaForm

def formulario_encuesta(request):
    if request.method == 'POST':
        form = EncuestaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gracias')
    else:
        form = EncuestaForm()
    return render(request, 'encuesta_form.html', {'form': form})

def gracias(request):
    return render(request, 'gracias.html')

# Definir una vista llamada home si se necesita
def home(request):
    return render(request, 'home.html')  # Asegúrate de tener una plantilla 'home.html'

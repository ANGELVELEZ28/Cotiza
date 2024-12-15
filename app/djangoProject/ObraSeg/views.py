from django.shortcuts import render
from .forms import CotizadorForm
# Create your views here.
def crear_cotizacion(request):
    if request.method == 'POST':
        form = CotizadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_cotizaciones')  # Cambia a la URL de tu lista de cotizaciones
    else:
        form = CotizadorForm()
    return render(request, 'crear_cotizacion.html', {'form': form})
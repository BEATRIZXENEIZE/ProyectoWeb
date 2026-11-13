from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Profesor
from .forms import ProfesorForm

def index(request):
    return render(request, 'inicio/index.html')

def profesores_list(request):
    profesores = Profesor.objects.all()
    form = ProfesorForm()

    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Profesor agregado exitosamente!')
            return redirect('profesores_list')
        else:
            messages.error(request, 'Por favor, corrige los errores en el formulario.')

    context = {
        'profesores': profesores,
        'form': form,
    }
    return render(request, 'inicio/profesores_abm.html', context)

def editar_profesor(request, id):
    profesor = get_object_or_404(Profesor, id=id)

    if request.method == 'POST':
        form = ProfesorForm(request.POST, instance=profesor)
        if form.is_valid():
            form.save()
            messages.success(request, f'¡Profesor "{profesor.nombre}" actualizado correctamente!')
            return redirect('profesores_list')
        else:
            messages.error(request, 'Por favor, corrige los errores en el formulario.')
    else:
        form = ProfesorForm(instance=profesor)

    context = {
        'profesor': profesor,
        'form': form,
    }
    return render(request, 'inicio/profesor_editar.html', context)

def eliminar_profesor(request, id):
    profesor = get_object_or_404(Profesor, id=id)

    if request.method == 'POST':
        nombre = profesor.nombre
        profesor.delete()
        messages.success(request, f'Profesor "{nombre}" eliminado con éxito.')
        return redirect('profesores_list')

    context = {
        'profesor': profesor,
    }
    return render(request, 'inicio/profesor_confirmar_eliminar.html', context)

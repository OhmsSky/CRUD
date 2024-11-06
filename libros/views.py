from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Libro

# Create your views here.

# Vista Creación de tarea
def crear_libro(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo') #Obtenemos el valor del formulario
        autor = request.POST.get('autor')

#Creación de tarea en base de datos
        Libro.objects.create(titulo=titulo, autor=autor)
        return redirect('listar_libros') #Redirige a la lista de tareas después de crearla
    return render(request, 'crear.html') #Mostrar el formulario en caso de GET

#Vista para actualizar una tarea existente
def actualizar_libro(request, id):
    libro = get_object_or_404(Libro, id=id) #Busca la tarea por ID
    if request.method == 'POST':
        libro.titulo = request.POST.get('titulo')
        libro.autor = request.POST.get('autor')
        libro.save() #Guardamos los cambios en la base de datos
        return redirect('listar_libro') #Redirige a la lista de tareas después de actualizar
    return render(request, 'actualizar_libro.html', {'libro':libro}) #Mostramos el formulario pre-llenado

#Vista para eliminar una tarea existente
def eliminar_libro(request, id):
    libro = get_object_or_404(Libro, id=id) #Busca la tarea por ID
    if request.method == 'POST':
        libro.delete() #Elimina la tarea desde la base de datos
        return redirect('listar_libros') #Redirige a la lista de taeas después de eliminar
    return render(request, 'eliminar_libro.html', {'libro':libro}) #Muestra el formulario de confirmación

def litar_libros(request):
    libros = Libro.objects.select_related('usuario').filter(usuario=request.user)
    paginator = Paginator(libros, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'listar_libros.html', {'page_obj': page_obj})
from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarea

# Vista Creación de tarea
def crearTarea(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo') #Obtenemos el valor del formulario
        descripcion = request.POST.get('descripcion')

#Creación de tarea en base de datos
        Tarea.objects.create(titulo=titulo, descripcion=descripcion)
        return redirect('listar_tareas') #Redirige a la lista de tareas después de crearla
    return render(request, 'crear.html') #Mostrar el formulario en caso de GET

#Vista para listar todas las tareas
def listar_tareas(request):
    tareas = Tarea.objects.all() #Obtiene tareas de la base de datos
    return render(request, 'listar_tareas.html', {'tareas': tareas}) #Pasamos las tareas al template

#Vista para actualizar una tarea existente
def actualizar_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id) #Busca la tarea por ID
    if request.method == 'POST':
        tarea.titulo = request.POST.get('titulo')
        tarea.descripcion = request.POST.get('descripcion')
        tarea.save() #Guardamos los cambios en la base de datos
        return redirect('listar_tareas') #Redirige a la lista de tareas después de actualizar
    return render(request, 'actualizar_tarea.html', {'tarea':tarea}) #Mostramos el formulario pre-llenado

#Vista para eliminar una tarea existente
def eliminar_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id) #Busca la tarea por ID
    if request.method == 'POST':
        tarea.delete() #Elimina la tarea desde la base de datos
        return redirect('listar_tareas') #Redirige a la lista de taeas después de eliminar
    return render(request, 'eliminar_tarea.html', {'tarea':tarea}) #Muestra el formulario de confirmación
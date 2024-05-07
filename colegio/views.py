from django.shortcuts import render, get_object_or_404
from colegio.models import Usuario, Padre, Profesor, Alumno, Curso

def mostrarIndex(request):
    return render(request,'index.html')

def mostrarFormRegUsu(request):
    return render(request,'form_registrar_usuario.html')

def registrarUsuario(request):
    rut = request.POST['txtrut']
    con = request.POST['txtcon']
    tip = request.POST['cbotip']
    #print('Entre')
    usuario = Usuario(rut=rut, contraseña=con, tipo = tip)
    usuarios = Usuario.objects.all()
    for x in usuarios:
        print(rut)
        print(x.rut)
        if x.rut==rut:
            print("entre al if")
            datos = {'r':'Este usuario ya esta registrado, pruebe con otro rut'}
            return render(request, 'form_registrar_usuario.html',datos)
    if tip == 'Administrador':
        usuario.save()
    elif tip == 'Alumno':
        usuario.save()
        datos = {'usuario': usuario}
        return render(request,'form_registrar_alumno.html',datos)
    elif tip == 'Padre':
        usuario.save()
        datos = {'usuario': usuario}
        return render(request,'form_registrar_padre.html',datos)
    elif tip == 'Profesor':
        usuario.save()
        datos = {'usuario': usuario}
        return render(request,'form_registrar_profesor.html',datos)
    
    
    return render(request, 'form_registrar_usuario.html')

def registrar_alumno(request, id):
    usuario = Usuario.objects.get(id=id)
    nom = request.POST['txtnom']
    eda = request.POST['txteda']
    ema = request.POST['txtema']

    alumno = Alumno(usuario_id=usuario.id, nombre = nom, edad = eda, email = ema)
    alumno.save()
    datos = { 'r' : 'Alumno registrado correctamente',
              'r1': 'Volver'}
    return render(request, 'form_registrar_alumno.html',datos)

def registrar_profesor(request, id):
    usuario = Usuario.objects.get(id=id)
    nom = request.POST['txtnom']
    eda = request.POST['txteda']
    ema = request.POST['txtema']

    profesor = Profesor(usuario_id=usuario.id, nombre = nom, edad = eda, email = ema)
    profesor.save()
    datos = { 'r' : 'Profesor registrado correctamente',
              'r1': 'Volver'}
    return render(request, 'form_registrar_profesor.html',datos)

def verificarInicio(request):
    usuarios = Usuario.objects.all()
    rut = request.POST['txtrut']
    pas = request.POST['txtpas']
    for x in usuarios:
        usuario = Usuario.objects.get(id=x.id)
        if rut=='0101':
            datos = {'usuario':usuario}
            return render(request, 'menu_admin.html', datos)
        if x.rut==rut:
            usuario = Usuario.objects.get(id=x.id)
            alumno = Alumno.objects.get(usuario_id=x.id)
            datos = {'usuario':usuario,
                     'alumno':alumno}
            return render(request, 'detalle_alumno.html', datos)
    datos = {'r': 'Lo sentimos no existe este usuario, reintentelo'}
    return render(request, 'Index.html', datos)

def mostrarCrearCurso(request):
    profesores = Profesor.objects.all()
    datos = {'profesor': profesores}
    return render(request, 'form_crear_curso.html',datos)

def crearCurso(request):
    id_pro = request.POST['cbopro']
    nom = request.POST['txtnom']
    profesor = Profesor.objects.get(id=id_pro)
    curso = Curso(nombre=nom,profesor_id=id_pro)
    curso.save()
    datos = { 'profesor': profesor,
             'curso':curso
             }
    return render(request, 'detalle_curso.html',datos)
    

from django.db import models

class Usuario(models.Model):
    rut = models.TextField(max_length=50)
    contraseña = models.TextField(max_length=50)
    tipo = models.TextField(max_length=50)

class Persona(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, null=True, blank=True, default="")
    nombre = models.TextField(max_length=50)
    edad = models.PositiveIntegerField(null=False, default=1)
    email = models.TextField(default="")

    class Meta:
        abstract = True

class Padre(Persona):
    hijos = models.ManyToManyField('Alumno', related_name='padres')

    def __str__(self):
        return f"{self.nombre} ({self.edad}) - {self.email}"

class Profesor(Persona):
    pass

    def __str__(self):
        return f"{self.nombre} ({self.edad})"

class Alumno(Persona):
    curso = models.ForeignKey('Curso', on_delete=models.CASCADE, related_name='alumnos', null=True, blank=True, default=None)

    def __str__(self):
        return f"{self.nombre} ({self.edad}) - {self.email} - {self.curso.nombre}"

class Curso(models.Model):
    nombre = models.TextField(max_length=50)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, related_name='cursos', default="")

    def __str__(self):
        return f"{self.nombre} ({self.profesor.nombre})"

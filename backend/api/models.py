from django.db import models

# Create your models here.
# Modelo de usuarios
class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)
# Modelo de Salones
class Classroom(models.Model):
    numCr = models.IntegerField()
    build = models.BooleanField()
# Modelo de Salones en uso
class InUseClassroom(models.Model):
    cr = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    time = models.IntegerField()
    inCharge = models.ForeignKey(User, on_delete=models.CASCADE)
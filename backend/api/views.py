from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.decorators import api_view

from .models import *
from .serializers import *

#Metodos de los usuarios
@api_view(['GET'])
def getUsers(request):
    user = User.objects.all()
    serializer = UserSerializer(user, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def postUser(request):
    data = request.data
    user = User.objects.create(
        name = data['name'],
        email = data['email'],
        password = data['password']
    )
    serializer = UserSerializer(user, many = False)
    return Response(serializer.data)

@api_view(['PUT'])
def putUser(request, pk):
    data = request.data
    user = User.objects.get(id=pk)
    serializer = UserSerializer(instance = user, data = data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
@api_view(['DELETE'])
def deleteUser(request, pk):
    user = User.objects.get(id=pk)
    user.delete()
    return Response("Elemento eliminado")

#Metodos de las aulas
@api_view(['GET'])
def getCrs(request):
    cr = Classroom.objects.all()
    serializer = ClassroomSerializer(cr, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def postCr(request):
    data = request.data
    cr = Classroom.objects.create(
        numCr = data['numCr'],
        build = data['build'],
    )
    serializer = ClassroomSerializer(cr, many = False)
    return Response(serializer.data)

@api_view(['PUT'])
def putCr(request, pk):
    data = request.data
    cr = Classroom.objects.get(id=pk)
    serializer = ClassroomSerializer(instance = cr, data = data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
@api_view(['DELETE'])
def deleteCr(request, pk):
    cr = Classroom.objects.get(id=pk)
    cr.delete()
    return Response("Elemento eliminado")

#Metodos de las aulas en uso
@api_view(['GET'])
def getIUCrs(request):
    iucr = InUseClassroom.objects.all()
    serializer = InUseClassroomSerializer(iucr, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def getIUCrsByUser(request, pk):
    iucr = InUseClassroom.objects.filter(inCharge=pk)
    serializer = InUseClassroomSerializer(iucr, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def getIUCrsByNum(request, pk):
    iucr = InUseClassroom.objects.filter(cr=pk)
    serializer = InUseClassroomSerializer(iucr, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def getIUCrsByTime(request, pk):
    iucr = InUseClassroom.objects.filter(time=pk)
    serializer = InUseClassroomSerializer(iucr, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def postIUCr(request):
    data = request.data
    filter = InUseClassroom.objects.filter(cr_id=data['cr']).filter(time=data['time'])
    if len(filter) > 0:
        return Response("El aula esta en uso")
    else:
        iucr = InUseClassroom.objects.create(
            cr_id = data['cr'],
            time = data['time'],
            inCharge_id = data ['inCharge'],
        )
        serializer = InUseClassroomSerializer(iucr, many = False)
        return Response(serializer.data)

@api_view(['PUT'])
def putIUCr(request, pk):
    data = request.data
    iucr = InUseClassroom.objects.get(id=pk)
    serializer = InUseClassroomSerializer(instance = iucr, data = data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response("No valido")
    
@api_view(['DELETE'])
def deleteIUCr(request, pk):
    cr = InUseClassroom.objects.get(id=pk)
    cr.delete()
    return Response("Elemento eliminado")
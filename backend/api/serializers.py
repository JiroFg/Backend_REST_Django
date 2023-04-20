from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'password')

class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ('id', 'numCr', 'build')

class InUseClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = InUseClassroom
        fields = ('id', 'cr', 'time', 'inCharge')
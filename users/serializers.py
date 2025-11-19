from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import CustomUser, Profesional

class ProfesionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesional
        fields = ['id', 'nombre', 'apellido', 'profesion']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "username", "rut", "rutdef", "profesional", "cesfam", "seccioncesfam", "created_at"]


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ["username","password","rut","rutdef","profesional","cesfam","seccioncesfam"]

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data["username"], password=data["password"])
        if user:
            return user
        raise serializers.ValidationError("Credenciales inválidas")
    

from rest_framework import serializers
from .models import Teacher


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('id', 'teacher', 'profession', 'is_active')


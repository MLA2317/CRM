from rest_framework import serializers
from .models import TeamGroup
from app.student.serializers import StudentPaymentSerializer
from app.teacher.serializers import TeacherSerializer


class TeamGroupCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamGroup
        fields = (
            'title', 'direction', 'teacher', 'students', 'image', 'room', 'day', 'is_active', 'time', 'updated_at',
            'created_at')


class TeamGroupSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer()
    students = StudentPaymentSerializer(many=True, read_only=True)
    # students = serializers.StringRelatedField(many=True)
    # students = serializers.PrimaryKeyRelatedField(read_only=True, many=True)

    class Meta:
        model = TeamGroup
        fields = (
            'id', 'title', 'direction', 'image', 'room', 'day',
            'is_active', 'time', 'updated_at',
            'created_at', 'teacher', 'students')

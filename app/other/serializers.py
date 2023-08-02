from rest_framework import serializers
from .models import Profession, Advertising, WhereCome, DayName, Course, Room


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title', 'duration', 'payment', 'lesson_duration', 'is_active', 'created_at')


class AdvertisingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertising
        fields = ('id', 'title')


# class WhereComeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = WhereCome
#         fields = ('id', 'student', 'advertising', 'is_active', 'created_at')
#

class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = ('id', 'title', 'is_active')


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'title', 'is_active')


class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = DayName
        fields = ('id', 'title', 'is_active')

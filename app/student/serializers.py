from rest_framework import serializers

from app.account.serializers import AccountsSerializer
from app.other.serializers import ProfessionSerializer
from .models import Student


class StudentPaymentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = (
            'student',
            'profession',
            'payment',
            'is_active',
            'date_created'
        )


class StudentPaymentSerializer(serializers.ModelSerializer):
    student = AccountsSerializer(read_only=True)
    profession = ProfessionSerializer(read_only=True)

    class Meta:
        model = Student
        fields = (
            'id',
            'student',
            'profession',
            'payment',
            'is_active'
        )


class StudentSerializer(serializers.ModelSerializer):
    student = AccountsSerializer(read_only=True)
    profession = ProfessionSerializer(read_only=True)

    pass
    # class Meta:
    #     model = StudentPayment
    #     fields = ('id')

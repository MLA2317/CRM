from rest_framework import generics

from app.account.permissons import IsAuthenticated, IsAdminUserForAccount
from .models import Student
from .serializers import StudentPaymentSerializer

class StudentPaymentListAPIView(generics.ListAPIView):
    queryset = Student.objects.filter(is_active=True).order_by('-id')
    serializer_class = StudentPaymentSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = None


class StudentPaymentCreateAPIView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentPaymentSerializer
    permission_classes = (IsAdminUserForAccount,)


class StudentPaymentRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentPaymentSerializer
    permission_classes = (IsAdminUserForAccount,)
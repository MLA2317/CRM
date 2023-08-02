from rest_framework import generics
from .models import Teacher
from .serializers import TeacherSerializer
from app.account.permissons import IsAuthenticated, IsAdminUserForAccount

class TeacherCreateAPIView(generics.CreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = (IsAdminUserForAccount,)


class TeacherListAPIView(generics.ListAPIView):
    queryset = Teacher.objects.filter(is_active=True).order_by('-id')
    serializer_class = TeacherSerializer
    permission_classes = (IsAdminUserForAccount,)
    pagination_class = None


class TeacherRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = (IsAdminUserForAccount,)

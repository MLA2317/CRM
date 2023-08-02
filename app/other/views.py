from rest_framework import generics, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from app.account.permissons import IsAdminUserForAccount, IsAuthenticated
from .models import Course, Profession, Room, DayName, Advertising
from .serializers import CourseSerializer, ProfessionSerializer, RoomSerializer, DaySerializer, AdvertisingSerializer


class CourseListAPIView(generics.ListAPIView):
    queryset = Course.objects.filter(is_active=True).order_by('-id')
    serializer_class = CourseSerializer
    pagination_class = None


class CourseCreateAPIView(generics.CreateAPIView):
    queryset = Course.objects.filter(is_active=True).order_by('-id')
    serializer_class = CourseSerializer
    permission_classes = (IsAdminUserForAccount,)
    authentication_classes = [TokenAuthentication]


class CourseRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (IsAdminUserForAccount,)
    lookup_field = 'pk'


class ProfessionListAPIView(generics.ListAPIView):
    queryset = Profession.objects.filter(is_active=True)
    serializer_class = ProfessionSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = None


class ProfessionCreateAPIView(generics.CreateAPIView):
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer
    permission_classes = (IsAdminUserForAccount,)
    authentication_classes = [TokenAuthentication]


class ProfessionRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer
    permission_classes = (IsAdminUserForAccount,)


class RoomListAPIView(generics.ListAPIView):
    queryset = Room.objects.filter(is_active=True).order_by('-id')
    serializer_class = RoomSerializer
    permission_classes = (IsAdminUserForAccount,)
    pagination_class = None


class RoomCreateAPIView(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = (IsAdminUserForAccount,)


class RoomRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = (IsAdminUserForAccount,)


class AdvertisingListAPIView(generics.ListAPIView):
    queryset = Advertising.objects.filter(is_active=True).order_by('-id')
    serializer_class = AdvertisingSerializer
    permission_classes = (IsAuthenticated,)


class AdvertisingCreateAPIView(generics.CreateAPIView):
    queryset = Advertising.objects.all()
    serializer_class = AdvertisingSerializer
    permission_classes = (IsAdminUserForAccount,)


class AdvertisingRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Advertising.objects.all()
    serializer_class = AdvertisingSerializer
    permission_classes = (IsAdminUserForAccount,)


# class WhereComeListAPIView(generics.ListAPIView):
#     queryset = WhereCome.objects.filter(is_active=True).order_by('-id')
#     serializer_class = WhereComeSerializer
#     permission_classes = (IsAuthenticated,)
#     pagination_class = None


# class WhereComeCreateAPIView(generics.CreateAPIView):
#     queryset = WhereCome.objects.all()
#     serializer_class = WhereComeSerializer
#     permission_classes = (IsAdminUserForAccount,)
#
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
#
#     def perform_create(self, serializer):
#         serializer.save()
#
#
# class WhereComeRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
#     queryset = WhereCome.objects.all()
#     serializer_class = WhereComeSerializer
#     permission_classes = (IsAdminUserForAccount,)


class DayNameListAPIView(generics.ListAPIView):
    queryset = DayName.objects.filter(is_active=True).order_by('-id')
    serializer_class = DaySerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = None


class DayNameCreateAPIView(generics.CreateAPIView):
    queryset = DayName.objects.all()
    serializer_class = DaySerializer
    permission_classes = (IsAdminUserForAccount,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()


class DayNameRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = DayName.objects.all()
    serializer_class = DaySerializer
    permission_classes = (IsAdminUserForAccount,)


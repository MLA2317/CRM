from rest_framework import generics, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from app.account.permissons import IsAdminUserForAccount, IsAuthenticated, IsOwnUserOrReadOnly
from app.group.models import TeamGroup
from .serializers import TeamGroupSerializer, TeamGroupCreateSerializer


class TeamGroupListAPIView(generics.ListAPIView):
    queryset = TeamGroup.objects.filter(is_active=True).order_by('-id')
    serializer_class = TeamGroupSerializer
    permission_classes = (IsAuthenticated, IsOwnUserOrReadOnly)
    pagination_class = None


class TeamGroupDestroyListAPIView(generics.ListAPIView):
    queryset = TeamGroup.objects.filter(is_active=False).order_by('-id')
    serializer_class = TeamGroupSerializer
    permission_classes = (IsAdminUserForAccount,)
    pagination_class = None


class TeamGroupCreateAPIView(generics.CreateAPIView):
    queryset = TeamGroup.objects.all()
    serializer_class = TeamGroupCreateSerializer
    permission_classes = (IsAdminUserForAccount, IsOwnUserOrReadOnly)
    authentication_classes = [TokenAuthentication]


class TeamGroupRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = TeamGroup.objects.all()
    serializer_class = TeamGroupCreateSerializer
    permission_classes = (IsAdminUserForAccount,)


class TeamDestroyView(generics.DestroyAPIView):
    queryset = TeamGroup.objects.all()
    serializer_class = TeamGroupSerializer
    permission_classes = (IsAdminUserForAccount,)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()


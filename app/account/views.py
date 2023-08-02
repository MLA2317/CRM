from rest_framework import generics, status
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .permissons import IsOwnUserOrReadOnly, IsAdminUserForAccount
from .serializers import RegisterSerializer, LoginSerializer, AccountsUpdateSerializer, ChangePasswordSerializer
from .models import Account


class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        print(serializer)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        phone = serializer.data.get('phone')
        tokens = Account.objects.get(phone=phone).tokens
        user_data['tokens'] = tokens
        return Response({'success': True, 'data': user_data}, status=status.HTTP_201_CREATED)


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'success': True, 'data': serializer.data}, status=status.HTTP_200_OK)


class AccountView(generics.GenericAPIView):
    permission_classes = (IsOwnUserOrReadOnly, IsAuthenticated)
    serializer_class = AccountsUpdateSerializer

    def get(self, request, *args, **kwargs):
        user = request.user
        query = Account.objects.get(id=user.id)
        serializer = self.get_serializer(query)
        return Response({'success': True, 'data': serializer.data}, status=status.HTTP_200_OK)


class AccountRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountsUpdateSerializer
    permission_classes = (IsOwnUserOrReadOnly, IsAuthenticated, IsAdminUserForAccount)

    def get(self, request, *args, **kwargs):
        query = self.get_object()
        if query:
            serializer = self.get_serializer(query)
            return Response({'success': True, 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'success': False, 'message': 'query did not exist'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = self.get_serializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True, 'data': serializer.data}, status=status.HTTP_202_ACCEPTED)
        return Response({'success': False, 'message': 'credentials is invalid'}, status=status.HTTP_404_NOT_FOUND)


class AccountAdminRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = AccountsUpdateSerializer
    queryset = Account.objects.all()
    permission_classes = (IsAdminUserForAccount, IsAdminUser)

    def get(self, request, *args, **kwargs):
        query = self.get_object()
        if query:
            serializer = self.get_serializer(query)
            return Response({'success': True, 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'success': False, 'message': 'query did not exist'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = self.get_serializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True, 'data': serializer.data}, status=status.HTTP_202_ACCEPTED)
        return Response({'success': False, 'message': 'credentials is invalid'}, status=status.HTTP_404_NOT_FOUND)


class AccountListApiView(generics.ListAPIView):
    queryset = Account.objects.filter(is_active=True).order_by('-id')
    serializer_class = AccountsUpdateSerializer
    permission_classes = (IsAuthenticated, IsOwnUserOrReadOnly)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class AccountDeleteListAPIView(generics.ListAPIView):  # for admin delete account
    queryset = Account.objects.filter(is_active=False).order_by('-id')
    serializer_class = AccountsUpdateSerializer
    permission_classes = (IsAdminUserForAccount,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class AccountDestroyView(generics.DestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountsUpdateSerializer
    permission_classes = (IsAdminUserForAccount,)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

    def perform_destroy(self, instance): # bu userni delete qilmaydi shuncha active ni False qilib qoyadi
        instance.is_active = False


class ChangePasswordViews(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = (IsOwnUserOrReadOnly, IsAuthenticated)

    def put(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={"request": self.request})
        if serializer.is_valid(raise_exception=True):
            return Response({'success': True, 'message': 'Successfully changed password'}, status=status.HTTP_200_OK)
        return Response({'success': False, 'message': 'Credentials is invalid'}, status=status.HTTP_400_BAD_REQUEST)




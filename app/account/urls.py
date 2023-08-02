from django.urls import path
from .views import RegisterView, LoginView, AccountView, AccountRetrieveUpdateView, ChangePasswordView, \
    AccountListApiView, AccountDestroyView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('profiles/', AccountListApiView.as_view()),
    path('profile/<int:pk>/', AccountView.as_view()),
    path('profile/update/<int:pk>/', AccountRetrieveUpdateView.as_view()),
    path('profile/delete/<int:pk>/', AccountDestroyView.as_view()),
    path('set-password/<int:pk>/', ChangePasswordView.as_view())
]



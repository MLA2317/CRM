from django.urls import path
from .views import StudentPaymentListAPIView, StudentPaymentCreateAPIView, StudentPaymentRetrieveUpdateAPIView

urlpatterns = [
    path('payment/', StudentPaymentListAPIView.as_view()),
    path('payment/create/', StudentPaymentCreateAPIView.as_view()),
    path('payment/<int:pk>/', StudentPaymentRetrieveUpdateAPIView.as_view())
]
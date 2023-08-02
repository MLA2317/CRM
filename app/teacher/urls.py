from django.urls import path
from .views import TeacherCreateAPIView, TeacherListAPIView, TeacherRetrieveUpdateAPIView

urlpatterns = [
    path('professions/', TeacherListAPIView.as_view()),
    path('profession/add', TeacherCreateAPIView.as_view()),
    path('professions/<int:pk>/', TeacherRetrieveUpdateAPIView.as_view()),
]

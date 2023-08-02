from django.urls import path

from .views import TeamGroupListAPIView, TeamGroupCreateAPIView, TeamGroupRetrieveUpdateAPIView, TeamDestroyView, \
        TeamGroupDestroyListAPIView


urlpatterns = [
        path('list/', TeamGroupListAPIView.as_view()),
        # path('deleted-list/', TeamGroupDestroyListAPIView.as_view()),
        path('add/', TeamGroupCreateAPIView.as_view()),
        path('edit/<int:pk>/', TeamGroupRetrieveUpdateAPIView.as_view()),
        path('delete/<int:pk>/', TeamDestroyView.as_view()),
]


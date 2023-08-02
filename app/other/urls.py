from django.urls import path
from .views import CourseCreateAPIView, CourseRetrieveUpdateAPIView, CourseListAPIView, ProfessionListAPIView, \
    ProfessionCreateAPIView, ProfessionRetrieveUpdateAPIView, RoomListAPIView, RoomCreateAPIView, \
    RoomRetrieveUpdateAPIView, AdvertisingListAPIView, AdvertisingCreateAPIView, AdvertisingRetrieveUpdateAPIView, \
    DayNameListAPIView, \
    DayNameCreateAPIView, DayNameRetrieveUpdateAPIView

# WhereComeCreateAPIView, WhereComeListAPIView, WhereComeRetrieveUpdateAPIView,\


urlpatterns = [
    # course
    path('courses/', CourseListAPIView.as_view()),
    path('course/add', CourseCreateAPIView.as_view()),
    path('course/<int:pk>/', CourseRetrieveUpdateAPIView.as_view()),

    # teacher profession
    path('teacher-professions/', ProfessionListAPIView.as_view()),
    path('teacher-profession/add/', ProfessionCreateAPIView.as_view()),
    path('teacher-profession/<int:pk>/', ProfessionRetrieveUpdateAPIView.as_view()),

    # room
    path('rooms/', RoomListAPIView.as_view()),
    path('room/add/', RoomCreateAPIView.as_view()),
    path('room/<int:pk>/', RoomRetrieveUpdateAPIView.as_view()),

    # advertising
    path('advertising/', AdvertisingListAPIView.as_view()),
    path('advertising/add/', AdvertisingCreateAPIView.as_view()),
    path('advertising/<int:pk>/', AdvertisingRetrieveUpdateAPIView.as_view()),

    # where comee
    # path('where-come/', WhereComeListAPIView.as_view()),
    # path('where-come/add/', WhereComeCreateAPIView.as_view()),
    # path('where-come/<int:pk>/', WhereComeRetrieveUpdateAPIView.as_view()),

    # day-name
    path('day/', DayNameListAPIView.as_view()),
    path('day/add/', DayNameCreateAPIView.as_view()),
    path('day/<int:pk>/', DayNameRetrieveUpdateAPIView.as_view()),
]

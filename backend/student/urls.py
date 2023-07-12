from django.urls import path

from .views import StudentListAPI, StudentDetail

urlpatterns = [
    path('list/', StudentListAPI.as_view(),                                                        name="student-list"),
    path('list/<int:pk>', StudentDetail.as_view(),                                               name="student-detail"),
]

from django.urls import path

from .views import SubjectListAPI, SubjectDetailAPI

urlpatterns = [
    path('list/', SubjectListAPI.as_view(),                                                        name="subject-list"),
    path('list/<int:pk>/', SubjectDetailAPI.as_view(),                                            name="subject-detail"),
]

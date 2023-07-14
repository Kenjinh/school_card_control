from django.urls import path

from .views import GradeListAPI, GradeDetailAPI, SchoolCardListAPI, SchoolCardDetailAPI

urlpatterns = [
    path('list/', SchoolCardListAPI.as_view(),                                                 name="school_card_list"),
    path('list/<int:pk>/', SchoolCardDetailAPI.as_view(),                                     name="school_card_detail"),
    path('grade/list/', GradeListAPI.as_view(),                                                      name="grade_list"),
    path('grade/list/<int:pk>/', GradeDetailAPI.as_view(),                                          name="grade_detail"),
]

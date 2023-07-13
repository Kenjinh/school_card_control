from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('student/', include('student.urls')),
    path('subject/', include('subject.urls')),
    path('school_card/', include('school_card.urls'))
]

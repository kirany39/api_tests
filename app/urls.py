from django.urls import path
from .views import *

urlpatterns = [
    path('student/', student_form, name='student_form'),
    path('success/', success, name='success'),
    path('student/create/', StudentCreateAPIView.as_view(), name='student_create'),
    path('student/update/<int:pk>/', StudentUpdateAPIView.as_view(), name='student_update'),
    path('student/delete/<int:pk>/', StudentDeleteAPIView.as_view(), name='student_delete'),
    path('student/list/', StudentListAPIView.as_view(), name='student_list'),
    path('bulk-import/', bulk_import_view, name='bulk_import'),
]

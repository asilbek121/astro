from django.urls import path
from . import views
from .views import Student_Register_Form

urlpatterns = [
    path('kurs', views.All_CourseList.as_view(), name='kurs'),
    path('<int:pk>Course_Detail', views.Course_Detail.as_view(), name='detail'),
    path('register', Student_Register_Form.as_view(), name='register'),
]
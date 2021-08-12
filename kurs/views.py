from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import Course, Student
# from kurs.models import Course


class All_CourseList(ListView):
    model = Course
    template_name = 'kurs/all_course.html'
    context_object_name = 'data'


class Course_Detail(DetailView):
    model = Course
    template_name = 'kurs/kurs_detail.html'
    context_object_name = 'data'


class Student_Register_Form(CreateView):
    model = Student
    template_name = 'kurs/reg.html'
    fields = ['last_name', 'first_name', 'age', 'phone', 'course']
    success_url = reverse_lazy('index')


def filter (request):
    kurslar = Course.objects.all()
    dict1 = {}
    nomer = 1
    for el in kurslar.values():
        studentlar = Student.objects.filter(course=el['id'])
        s = []
        for i in studentlar:
           s.append(i)
        nomer += 1
        dict1[el['name']] = s

    return render(request, 'kurs/student.html', {'dict1': dict1})

def reg(request):
    return render(request, 'kurs/reg.html')

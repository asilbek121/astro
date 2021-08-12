from .models import *

from django.contrib import admin
class Student_List(admin.TabularInline):
    model = Student


class Course_Admin(admin.ModelAdmin):
    inlines = [Student_List]

admin.site.register(Course, Course_Admin)
admin.site.register(Student)
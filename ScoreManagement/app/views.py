from django.shortcuts import render
from app.models import Student, Teacher, College, Major,\
    MajorPlan, MajorCourses, Teaching, AdmClass


def show_tables(request):
    college_list = College.objects.all()
    major_list = Major.objects.all()
    major_plan_list = MajorPlan.objects.all()
    adm_class_list = AdmClass.objects.all()
    student_list = Student.objects.all()

    context = {
        'college_list': college_list,
        'major_list': major_list,
        'major_plan_list': major_plan_list,
        'adm_class_list': adm_class_list,
        'student_list': student_list
    }

    return render(request, 'show_tables.html', context)


def login(request):
    pass


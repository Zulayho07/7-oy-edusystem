from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Student


def home(request):
    courses = Course.objects.all()
    students = Student.objects.all()

    context = {
        'courses': courses,
        'students': students,
        'total_students': students.count(),
        'title': 'Bosh sahifa',
    }
    return render(request, 'courses/index.html', context)


def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    students = course.students.all()
    courses = Course.objects.all()

    context = {
        'course': course,
        'students': students,
        'courses': courses,
        'title': course.name,
    }
    return render(request, 'courses/course_detail.html', context)


def student_detail(request, student_id):
    student = Student.objects.get(id=student_id)
    courses = Course.objects.filter(students=student)

    context = {
        'student': student,
        'courses': courses,
        'title': student.full_name,
    }
    return render(request, 'courses/student_detail.html', context)


@login_required(login_url='home')
def like_course(request, course_id):
    course = Course.objects.get(pk=course_id)

    student = Student.objects.first()

    if student in course.likes.all():
        course.likes.remove(student)
    else:
        course.likes.add(student)

    return redirect('course_detail', course_id=course.pk)
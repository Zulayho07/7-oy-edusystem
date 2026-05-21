from django.urls import path
from .views import home, course_detail, student_detail, like_course

urlpatterns = [
    path('', home, name='home'),
    path('courses/<int:course_id>/', course_detail, name='course_detail'),
    path('students/<int:student_id>/', student_detail, name='student_detail'),
    path('course/<int:course_id>/like/', like_course, name='like_course'),
]

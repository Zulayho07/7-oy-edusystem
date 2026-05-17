from django.urls import path
from . import views

urlpatterns = [
    path('',                                         views.home,           name='home'),
    path('courses/<int:course_id>/',                 views.course_detail,  name='course_detail'),
    path('students/<int:student_id>/',               views.student_detail, name='student_detail'),
    path('enroll/<int:course_id>/<int:student_id>/', views.enroll,         name='enroll'),
]
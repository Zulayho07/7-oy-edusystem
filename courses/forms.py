from django.forms import ModelForm

from django import forms

from courses.models import Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'course']
        widgets = {
            'course': forms.Select(attrs={'class': 'form-control'}),
        }
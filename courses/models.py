from django.db import models


class Student(models.Model):
    full_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.full_name

    def __repr__(self):
        return self.full_name


class Course(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    duration = models.CharField(max_length=50)

    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
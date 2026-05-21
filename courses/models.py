from django.db import models


class Student(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='F.I.Sh')
    age = models.PositiveIntegerField(verbose_name='Yoshi')
    gender=models.CharField(max_length=7, default='Male', verbose_name='Jinsi')
    phone_number = models.CharField(max_length=20, verbose_name='Telefon raqami')
    address = models.TextField(blank=True, null=True,  verbose_name='Manzili')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Ro\'yxatdan o\'tgan sana')

    def __str__(self):
        return self.full_name

    def __repr__(self):
        return self.full_name

    class Meta:
        verbose_name = "O'quvchi"
        verbose_name_plural = "O'quvchilar"


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nomi')
    description = models.TextField(blank=True, null=True, verbose_name='Batafsil')
    price = models.PositiveIntegerField(verbose_name='Narxi')
    duration = models.CharField(max_length=50, verbose_name='Davomiyligi')
    level=models.CharField(max_length=50, default='Beginner', verbose_name='Darajasi')
    is_active = models.BooleanField(default=True, verbose_name='Faolmi')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Oxirgi tahrirlangan vaqt')

    students = models.ManyToManyField(Student, verbose_name='O\'quvchilar')
    likes = models.ManyToManyField(Student, related_name='favorite_courses', blank=True, verbose_name='Yoqtirganlar')

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    class Meta:
        verbose_name = "Kurs"
        verbose_name_plural = "Kurslar"

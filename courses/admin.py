from django.contrib import admin
from django.forms import Textarea
from django.db.models import TextField

from .models import Course, Student, Comment

admin.site.site_header = 'Edusystem'
admin.site.site_title = 'edusystem'
admin.site.login_template = 'admin/login.html'
admin.site.logout_template = 'admin/logout.html'


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
    readonly_fields = ('user',)

    formfield_overrides = {
        TextField: {
            "widget": Textarea(attrs={
                "rows": 2,
                "cols": 40,
            })
        },
    }

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)

        for instance in instances:
            # yangi comment bo‘lsa user biriktiriladi
            if not instance.pk and not instance.user:
                instance.user = request.user

            instance.save()

        formset.save_m2m()


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration', 'description', 'check_active')
    list_display_links = ('name',)
    list_filter = ('duration',)
    list_editable = ('description',)
    search_fields = ('name', 'description')
    fieldsets = (
        ('Asosiy', {
            'fields': ('name', )
        }),
        ('Batafsil', {
            'fields': ('duration', 'price', 'level')
        }),
    )
    inlines = (CommentInline,)

    @admin.display(boolean=True, description='Faol')
    def check_active(self, obj):
        if obj.is_active:
            return True
        return False



class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'gender', 'phone_number')
    list_display_links = ('full_name',)
    list_filter = ('gender',)
    search_fields = ('full_name', 'phone_number')
    fields = ('full_name', 'phone_number')


admin.site.register(Student, StudentAdmin)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Student, Staff, Admin, Parent

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'is_student', 'is_staff_member', 'is_admin', 'is_parent')
    search_fields = ('email',)
    list_filter = ('is_student', 'is_staff_member', 'is_admin', 'is_parent')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('User Type', {'fields': ('is_student', 'is_staff_member', 'is_admin', 'is_parent')}),  # Fix this line
    )

admin.site.register(CustomUser, CustomUserAdmin)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'student_id')
    search_fields = ('user__email', 'student_id')

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('user', 'employee_id')
    search_fields = ('user__email', 'employee_id')

@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__email',)

@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__email',)

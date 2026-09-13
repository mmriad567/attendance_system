from django.contrib import admin
from .models import Teacher,ClassRoom,Student,Attendance

# Register your models here.

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display=('name','email','phone','joined_at')
    search_fields=('name','email')


@admin.register(ClassRoom)
class ClassRoomAdmin(admin.ModelAdmin):
    list_display=('name','section','teacher')
    list_filter=('name',)



@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=('roll_number','name','classroom','email')
    list_filter=('classroom',)
    search_fields=('name','roll_number')



@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display=('student','date','is_present','marked_by')
    list_filter=('date','is_present')
    search_fields=('student__name',)
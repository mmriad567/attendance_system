from django.shortcuts import render,redirect
from .models import Teacher,ClassRoom,Student,Attendance

# Create your views here.

def home(request):

    if not request.user.is_authenticated:
        return redirect('login')
    
    user=request.user

    if user.is_superuser:

        context={'total_teachers':Teacher.objects.count(),
                 'total_students':Student.objects.count(),
                 'total_classrooms':ClassRoom.objects.count(),
                 'total_attendances':Attendance.objects.count()
                 }

        return render(request,'attendance/admin_dashboard.html',context)

   

    if hasattr(user,'student'):
        return render(request,'attendance/student_dashboard.html')


    if hasattr(user,'teacher'):
        return render(request,'attendance/teacher_dashboard.html')

    return render(request,'attendance/home.html')

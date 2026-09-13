from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Teacher(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='teacher')
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=20,blank=True,null=True)
    joined_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    

class ClassRoom(models.Model):
    name=models.CharField(max_length=40)
    section=models.CharField(max_length=20)
    teacher=models.ForeignKey(Teacher,on_delete=models.SET_NULL,blank=True,null=True,related_name='classes')
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together=['name','section']

    def __str__(self):
        return f"{self.name} - {self.section}"



class Student(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='student')
    roll_number=models.CharField(max_length=20)
    name=models.CharField(max_length=100)
    classroom=models.ForeignKey(ClassRoom,on_delete=models.CASCADE,related_name='students')
    email=models.EmailField(blank=True,null=True)
    phone=models.CharField(max_length=20,blank=True,null=True)
    admission_date=models.DateTimeField(auto_now_add=True)


    class Meta:
        unique_together=['roll_number','classroom']

    def __str__(self):
        return f"{self.roll_number} - {self.name}"


class Attendance(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE,related_name='attendances')
    date=models.DateField()
    is_present=models.BooleanField(default=False)
    marked_by=models.ForeignKey(Teacher,on_delete=models.SET_NULL,blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together=['student','date']


    def __str__(self):
        status="present" if self.is_present else "Absent"
        return f"{self.student.name} - {self.date} - {status}"


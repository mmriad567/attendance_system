from django import forms
from django.contrib.auth.models import User
from .models import Teacher,Student


class TeacherForm(forms.ModelForm):
    class Meta:
        model=Teacher
        fields='__all__'

    def clean_user(self):
        user=self.cleaned_data.get('user')

        if hasattr(user,'student'):
            raise forms.ValidationError("এই ইউজার ইতিমধ্যে একজন Student। একজন ইউজার একইসাথে Teacher ও Student হতে পারবে না।")       
        return user


class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'

    def clean_user(self):
        user=self.cleaned_data.get('user')

        if hasattr(user,'teacher'):
            raise forms.ValidationError("এই ইউজার ইতিমধ্যে একজন Teacher। একজন ইউজার একইসাথে Teacher ও Student হতে পারবে না।")
        return user

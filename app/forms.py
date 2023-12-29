from django import forms
from .models import Student, Parent, Academic, Documents

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class ParentForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields = '__all__'

class AcademicForm(forms.ModelForm):
    class Meta:
        model = Academic
        fields = '__all__'

class DocumentsForm(forms.ModelForm):
    class Meta:
        model = Documents
        fields = '__all__'

from django.shortcuts import render, redirect
from .forms import StudentForm, ParentForm, AcademicForm, DocumentsForm

def student_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # You can define a success URL
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})

# Similar views for other forms (parent_form, academic_form, documents_form) with appropriate form names.

def success(request):
    return render(request, 'success.html')


from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer

class StudentCreateAPIView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentUpdateAPIView(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDeleteAPIView(generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentListAPIView(generics.ListAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        queryset = Student.objects.all()
        class_param = self.request.query_params.get('class', None)
        section_param = self.request.query_params.get('section', None)
        father_name_param = self.request.query_params.get('father_name', None)

        if class_param:
            queryset = queryset.filter(academic__class_field=class_param)

        if section_param:
            queryset = queryset.filter(academic__section=section_param)

        if father_name_param:
            queryset = queryset.filter(parent__father_name=father_name_param)

        return queryset

from django.shortcuts import render
from django.contrib import messages
from .tasks import insert_random_data

def bulk_import_view(request):
    if request.method == 'POST' and request.FILES['csv_file']:
        csv_file = request.FILES['csv_file']
        # Your logic to process the CSV file, extract data, and save it to the database
        # For simplicity, this example triggers the Celery task to insert random data
        insert_random_data.delay()
        messages.success(request, 'Bulk import started. Check the task logs for progress.')
    return render(request, 'bulk_import.html')

# yourappname/views.py
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import StudentForm

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            # Email sending logic is now handled in the model's save method
            return redirect('success')  # You can define a success URL
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})

# yourappname/models.py
from django.db import models
from django.core.mail import send_mail
from django.utils import timezone

class Student(models.Model):
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    adhar_card_number = models.CharField(max_length=16)
    dob = models.DateField()
    category = models.CharField(max_length=50)
    height = models.FloatField()
    weight = models.FloatField()
    mail_id = models.EmailField()
    contact_detail = models.CharField(max_length=20)
    address = models.TextField()

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)
        
        # Send email only when a new student is created
        if is_new:
            self.send_enrollment_notification()

    def send_enrollment_notification(self):
        subject = 'New Enrollment Notification'
        message = f'Dear {self.name},\n\nThank you for enrolling in our program!'
        from_email = 'webmaster@example.com'  # Update with your email address
        recipient_list = [self.mail_id, 'durganand.jha@habrie.com']  # Add other recipients as needed

        send_mail(subject, message, from_email, recipient_list)

class Parent(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    father_name = models.CharField(max_length=255)
    father_qualification = models.CharField(max_length=100)
    father_profession = models.CharField(max_length=100)
    father_mobile_number = models.CharField(max_length=20)
    father_mail_id = models.EmailField()
    mother_name = models.CharField(max_length=255)
    mother_qualification = models.CharField(max_length=100)
    mother_profession = models.CharField(max_length=100)
    mother_mobile_number = models.CharField(max_length=20)
    mother_mail_id = models.EmailField()

class Academic(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    enrollment_id = models.CharField(max_length=255)
    class_field = models.CharField(max_length=50)
    section = models.CharField(max_length=10)
    doj = models.DateField(default=timezone.now)

class Documents(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    documents = models.FileField(upload_to='documents/')
    # Add any additional fields for documents if needed

# yourappname/tasks.py
from celery import shared_task
from .models import Student
from faker import Faker
import random

@shared_task
def insert_random_data():
    fake = Faker()
    
    for _ in range(100):  # Adjust the number of records as needed
        student = Student.objects.create(
            name=fake.name(),
            gender=random.choice(['Male', 'Female']),
            adhar_card_number=fake.uuid4(),
            dob=fake.date_of_birth(),
            category=random.choice(['Category1', 'Category2']),
            height=random.uniform(150, 200),
            weight=random.uniform(40, 100),
            mail_id=fake.email(),
            contact_detail=fake.phone_number(),
            address=fake.address(),
        )

        # Similar logic for Parent, Academic, and Documents models if needed
        # Example: Parent.objects.create(student=student, ...)

    return "Random data inserted successfully."

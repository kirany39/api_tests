# Generated by Django 5.0 on 2023-12-29 11:04

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=10)),
                ('adhar_card_number', models.CharField(max_length=16)),
                ('dob', models.DateField()),
                ('category', models.CharField(max_length=50)),
                ('height', models.FloatField()),
                ('weight', models.FloatField()),
                ('mail_id', models.EmailField(max_length=254)),
                ('contact_detail', models.CharField(max_length=20)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('father_name', models.CharField(max_length=255)),
                ('father_qualification', models.CharField(max_length=100)),
                ('father_profession', models.CharField(max_length=100)),
                ('father_mobile_number', models.CharField(max_length=20)),
                ('father_mail_id', models.EmailField(max_length=254)),
                ('mother_name', models.CharField(max_length=255)),
                ('mother_qualification', models.CharField(max_length=100)),
                ('mother_profession', models.CharField(max_length=100)),
                ('mother_mobile_number', models.CharField(max_length=20)),
                ('mother_mail_id', models.EmailField(max_length=254)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.student')),
            ],
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documents', models.FileField(upload_to='documents/')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.student')),
            ],
        ),
        migrations.CreateModel(
            name='Academic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrollment_id', models.CharField(max_length=255)),
                ('class_field', models.CharField(max_length=50)),
                ('section', models.CharField(max_length=10)),
                ('doj', models.DateField(default=django.utils.timezone.now)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.student')),
            ],
        ),
    ]
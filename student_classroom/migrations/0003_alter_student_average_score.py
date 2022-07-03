# Generated by Django 4.0.2 on 2022-05-23 10:38

from django.db import migrations, models
import student_classroom.models


class Migration(migrations.Migration):

    dependencies = [
        ('student_classroom', '0002_classroom_student_student_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='average_score',
            field=models.FloatField(blank=True, null=True, validators=[student_classroom.models.avg_score_validator]),
        ),
    ]
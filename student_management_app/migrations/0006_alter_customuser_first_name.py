# Generated by Django 5.0.4 on 2024-05-03 17:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("student_management_app", "0005_studentresult"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="first_name",
            field=models.CharField(
                blank=True, max_length=150, verbose_name="first name"
            ),
        ),
    ]

# Generated by Django 4.2.2 on 2023-08-16 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LRS_App', '0007_alter_uploadedfile_uploaded_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedfile',
            name='uploaded_datetime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

# Generated by Django 5.0.4 on 2024-12-05 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='Email_Id',
            new_name='Email',
        ),
    ]

# Generated by Django 4.1.4 on 2023-03-07 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0003_alter_skill_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='user',
        ),
    ]
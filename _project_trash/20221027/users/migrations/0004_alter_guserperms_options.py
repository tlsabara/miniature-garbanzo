# Generated by Django 4.1.2 on 2022-10-15 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_garbanzoperms_sys_name_gperms_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='guserperms',
            options={'managed': False},
        ),
    ]

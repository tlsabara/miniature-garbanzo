# Generated by Django 4.1.2 on 2022-10-15 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_garbanzoperms_long_desc_gperms_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='garbanzoperms',
            name='system_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='garbanzouser',
            name='system_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='historicalgarbanzoperms',
            name='system_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='historicalgarbanzouser',
            name='system_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='historicalguserperms',
            name='system_active',
            field=models.BooleanField(default=True),
        ),
    ]
# Generated by Django 4.1.2 on 2022-10-15 23:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_testeid'),
    ]

    operations = [
        migrations.CreateModel(
            name='TesteFkId',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teste', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.testeid')),
            ],
        ),
    ]
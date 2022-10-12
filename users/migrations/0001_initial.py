# Generated by Django 4.1.2 on 2022-10-12 02:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import miniature_garbanzo.utils.validators
import simple_history.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='GarbanzoUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('system_create_at', models.DateTimeField(auto_now_add=True)),
                ('system_edited_at', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('nome_completo_guser', models.CharField(max_length=255)),
                ('dt_nasc_guser', models.DateField(blank=True, null=True)),
                ('cpf_guser', models.CharField(max_length=11, validators=[miniature_garbanzo.utils.validators.validacao_apenas_numeros, miniature_garbanzo.utils.validators.validacao_onze_digitos])),
                ('num_doc_guser', models.CharField(blank=True, max_length=30, null=True)),
                ('genero_guser', models.CharField(blank=True, choices=[('masculino', 'Masculino'), ('feminino', 'Feminino'), ('nao_me_identifico', 'Não me identifico'), ('prefiro_nao_informar', 'Prefiro não informar'), ('outro', 'Outro')], max_length=30, null=True)),
                ('observacoes_guser', models.TextField(blank=True, max_length=1000, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HistoricalGarbanzoUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('pkid', models.BigIntegerField(blank=True, db_index=True, editable=False)),
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('system_create_at', models.DateTimeField(blank=True, editable=False)),
                ('system_edited_at', models.DateTimeField(blank=True, editable=False)),
                ('email', models.EmailField(db_index=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('nome_completo_guser', models.CharField(max_length=255)),
                ('dt_nasc_guser', models.DateField(blank=True, null=True)),
                ('cpf_guser', models.CharField(max_length=11, validators=[miniature_garbanzo.utils.validators.validacao_apenas_numeros, miniature_garbanzo.utils.validators.validacao_onze_digitos])),
                ('num_doc_guser', models.CharField(blank=True, max_length=30, null=True)),
                ('genero_guser', models.CharField(blank=True, choices=[('masculino', 'Masculino'), ('feminino', 'Feminino'), ('nao_me_identifico', 'Não me identifico'), ('prefiro_nao_informar', 'Prefiro não informar'), ('outro', 'Outro')], max_length=30, null=True)),
                ('observacoes_guser', models.TextField(blank=True, max_length=1000, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical garbanzo user',
                'verbose_name_plural': 'historical garbanzo users',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]

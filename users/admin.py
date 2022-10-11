from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .forms import GarbanzoUserChangeForm, GarbanzoUserCreationForm
from .models import GarbanzoUser


class CustomUserAdmin(UserAdmin):
    """
    Classe para configurar o model para o Django Admin.
    """
    add_form = GarbanzoUserCreationForm
    form = GarbanzoUserChangeForm
    model = GarbanzoUser
    readonly_fields = ('id',)
    list_display = ('nome_completo_guser', 'email', 'id', 'is_staff', 'is_active',)
    list_filter = ('nome_completo_guser', 'email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'id', 'nome_completo_guser', 'cpf_guser')}),
        ('Acesso Django Admin', {'fields': ('is_staff', 'is_active')}),
        ('Dados do Colaborador', {'fields': ('dt_nasc_guser', 'num_doc_guser', 'cargo_guser', 'setor_guser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(GarbanzoUser, CustomUserAdmin)


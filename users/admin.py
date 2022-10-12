from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

# Register your models here.
from .forms import GarbanzoUserChangeForm, GarbanzoUserCreationForm
from .models import GarbanzoUser

from miniature_garbanzo.utils import functions


class CustomUserHistoryAdmin(SimpleHistoryAdmin):
    list_display = ("id", "nome_completo_guser", "status", 'user__username')
    history_readonly_fields = ('id', 'email')
    history_list_display = ("nome_completo_guser", '')


class CustomUserAdmin(CustomUserHistoryAdmin):
    """
    Classe para configurar o model para o Django Admin.

    Testes de uso do SimpleHistoryAdmin no lugar de UserAdmin
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
        ('Dados do Colaborador', {'fields': ('dt_nasc_guser', 'num_doc_guser', 'genero_guser',)}),
        ('Observações', {'fields': ('observacoes_guser',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)

    def save_model(self, request, obj, form, change):
        """
        Fazendo o override para tratar da criação de senha.
        :param request:
        :param obj:
        :param form:
        :param change:
        :return:
        """
        if obj.password is None:
            senha_nova = functions.gerador_pwd(8)
            obj.set_password(senha_nova)
            obj.observacoes_guser = f'{obj.observacoes_guser}\n\n ---\n Nova Senha: {senha_nova}'

        super().save_model(request, obj, form, change)


admin.site.register(GarbanzoUser, CustomUserAdmin)

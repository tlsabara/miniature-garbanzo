from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from core.models import GarbanzoPerms
# Register your models here.
from users.forms import GarbanzoUserChangeForm, GarbanzoUserCreationForm
from users.models import GarbanzoUser, GUserPerms, Employee


class CustomUserHistoryAdmin(SimpleHistoryAdmin):
    list_display = ("id", "status", 'user__username')
    history_list_display = ("nome_completo_guser",)
    history_readonly_fields = (
        'id',
        'nome_completo_guser',
        'cpf_guser',
        'email',
    )


class PermissionInline(admin.TabularInline):
    model = GUserPerms


class EmployeeLinked(admin.StackedInline):
    model = Employee

class CustomUserAdmin(CustomUserHistoryAdmin):
    """
    Classe para configurar o model para o Django Admin.

    Testes de uso do SimpleHistoryAdmin no lugar de UserAdmin
    """
    inlines = [
        EmployeeLinked,
        PermissionInline
    ]
    add_form = GarbanzoUserCreationForm
    form = GarbanzoUserChangeForm
    model = GarbanzoUser
    readonly_fields = ('id',)
    list_display = ('nome_completo_guser', 'email', 'id', 'is_staff', 'is_active',)
    list_filter = ('nome_completo_guser', 'email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'id', 'nome_completo_guser', 'cpf_guser', 'system_active')}),
        ('Acesso Django Admin', {'fields': ('is_staff', 'is_active')}),
        ('Dados do Colaborador', {'fields': ('dt_nasc_guser', 'num_doc_guser', 'genero_guser',)}),
        ('Observações', {'fields': ('observacoes_guser',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'observacoes_guser')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


class CurtomGUserPermsAdmin(SimpleHistoryAdmin):
    list_display = ('__str__', 'id_guser', 'id_gperms', 'id', 'system_active')
    list_filter = ('id_guser', 'id_gperms__app_gperms')


admin.site.register(GUserPerms, CurtomGUserPermsAdmin)
admin.site.register(GarbanzoUser, CustomUserAdmin)

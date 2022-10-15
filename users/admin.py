from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

# Register your models here.
from .forms import GarbanzoUserChangeForm, GarbanzoUserCreationForm
from .models import GarbanzoUser, GarbanzoPerms, GUserPerms, GarbanzoAssetType, GarbanzoAssetItem, GarbanzoLinkType, TesteId, TesteFkId

from miniature_garbanzo.utils import functions


class CustomUserHistoryAdmin(SimpleHistoryAdmin):
    list_display = ("id", "status", 'user__username')
    history_list_display = ("nome_completo_guser",)
    history_readonly_fields = (
        'id',
        'nome_completo_guser',
        'cpf_guser',
        'email',
    )

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
    list_filter = ('id_guser', 'id_gperms')


class CustomGarbanzoPermsAdmin(SimpleHistoryAdmin):
    list_display = ('sys_name_gperms', 'desc_gperms', 'long_desc_gperms', 'id', 'system_active' )
    list_filter = ('sys_name_gperms',)


class CustomGarbanzoAssetAdmin(SimpleHistoryAdmin):
    history_readonly_fields = ('id', 'name_item')


admin.site.register(GarbanzoPerms, CustomGarbanzoPermsAdmin)
admin.site.register(GUserPerms, CurtomGUserPermsAdmin)
admin.site.register(GarbanzoUser, CustomUserAdmin)
admin.site.register(GarbanzoAssetItem, CustomGarbanzoAssetAdmin)
admin.site.register(GarbanzoLinkType, SimpleHistoryAdmin)
admin.site.register(GarbanzoAssetType,SimpleHistoryAdmin)
admin.site.register(TesteId,SimpleHistoryAdmin)
admin.site.register(TesteFkId,SimpleHistoryAdmin)

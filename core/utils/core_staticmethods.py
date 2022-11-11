"""
Métodos e funções que o App Core, utilzia?
"""


def gerador_menu_dict(queryset: object) -> dict:
    """
    Gerador do dict para montar o menu
    """
    if len(queryset) == 1:
        return {'has_perms': False, 'perm_list': []}


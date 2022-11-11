import pytest

from ..utils import core_staticmethods


def test_geradormenudict_return_dict_when_queryset_has_no_perms(fxt_dict_greradormenudict_with_no_perms):
    assert isinstance(core_staticmethods.gerador_menu_dict(), dict)
    assert core_staticmethods.gerador_menu_dict([]) == fxt_dict_greradormenudict_with_no_perms


def test_geradormenudict_return_dict_with_has_perms():
    assert isinstance(core_staticmethods.gerador_menu_dict(), dict)
    assert False

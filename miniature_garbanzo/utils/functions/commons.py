from random import choice
import string

ESPECIAIS = '=+-_)(*&$#@!<>?'
PARAMS = [
    '-l', '--length',
    '-s', '--start',
    '-e', '--end',
    '-q', '--qty'
]

CARACTERES = string.ascii_lowercase + ESPECIAIS + string.digits + string.ascii_uppercase + string.digits + ESPECIAIS


def gerador_pwd(len_senha, prefix='', sufix=''):
    passwd = ''
    for i in range(len_senha):
        passwd += choice(CARACTERES)
    return prefix + passwd + sufix

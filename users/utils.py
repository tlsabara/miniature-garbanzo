

# fixme mudar para um módulo igual ao da classe de assets
class AppUserChoices:
    class Commons:
        GENERO = [
            ("masculino", "Masculino"),
            ("feminino", "Feminino"),
            ("nao_me_identifico", "Não me identifico"),
            ("prefiro_nao_informar", "Prefiro não informar"),
            ("outro", "Outro"),
        ]

        TIPO_RESIDENCIA = [
            ("casa", "Casa"),
            ("apartamento", "Apartamento"),
            ("outro", "Outro"),
        ]

    class GarbanzoUserChoices:
        TIPO = [
            ("colaborador", "Colaborador"),  # Não tem acesso ao sistema
            ("utilizador", "Utilizador"),  # Tem acesso mas apenas aos seus dados
            (
                "moderador",
                "Moderador",
            ),  # Tem acesso aos dados de todos, se as Permissões concederem
            (
                "app_admin",
                "Administrador da aplicação",
            ),  # Tem acesso irrestrito, mas não altera itens do Server Admin
            ("server_admin", "Administrador do servidor"),  # Tem acesso irrestrito
        ]

import flet as ft
from flet import AppBar, Text, View
from flet.auth import user
from flet.core import page
from flet.core.colors import Colors

import lista


class User():
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo
    
    
    
def main(page: ft.Page):
    # Configurações
    page.title = "Exemplo de Rotas"
    page.theme_mode = ft.ThemeMode.DARK  # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    # Funções

    lista = []
def salvar_nome(e):
        lista.append(input_nome.value)
        input_nome.value = ''
        page.overlay.append(msg_sucesso)
        msg_sucesso.open = True
        page.update() 
        
    else:
        obj_user = User
            nome=input_nome.value
            salario=0,
            cargo= "instrutor"
        )
        lista.append(obj_user)
        input_nome.value = ''
        page.overlay.append(msg_sucesso)
        msg_sucesso.open = True
        page.update() 
        

    def exibir_lista(e):
        lv_nome.controls.clear()
        for nome in lista:
            lv_nome.controls.append(
                ft.Text(value=f"{user.nome} - {user.salario} - {user.cargo}")
            )
        page.update()


    def gerencia_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Home"), bgcolor=Colors.PRIMARY_CONTAINER),
                    input_nome,
                    ft.Button(
                        text='Salvar',
                        on_click=lambda _: salvar_nome(e)
                    ),
                    ft.Button(
                        text='Exibir listas',
                        on_click=lambda _: page.go("/segunda"),
                    )
                ],
            )
        )
        if page.route == "/segunda":
            exibir_lista(e)
            page.views.append(
                View(
                    "/segunda",
                    [
                        AppBar(title=Text("Segunda tela"), bgcolor=Colors.SECONDARY_CONTAINER),
                        lv_nome,
                    ],
                )
            )
        page.update()

    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)


    # Componentes
    msg_sucesso = ft.SnackBar(
        content=ft.Text("Nome salvo com sucesso!!"),
        bgcolor=Colors.WHITE,
    )



    input_nome = ft.TextField(label='Nome:', hint_text='EX: Lorena ')

    lv_nome = ft.ListView(
        height=500
    )



    # Eventos
    page.on_route_change = gerencia_rotas
    page.on_view_pop = voltar

    page.go(page.route)

# Comando que executa o aplicativo
# Deve estar sempre colado na linha
ft.app(main)
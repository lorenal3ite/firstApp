import flet as ft
from flet.core.app_bar import AppBar
from flet.core.colors import Colors
from flet.core.elevated_button import ElevatedButton
from flet.core.page import Page
from flet.core.text import Text
from flet.core.view import View


def main(page: Page):
    # config da pagina
    page.title = "Exemplo de rotas"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    def gerencia_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Cadastro de livros "), bgcolor=Colors.PRIMARY_CONTAINER),
                    input_titulo, input_descricao, input_categoria, input_autor,
                    ElevatedButton(text="Cadastrar livro ", on_click=lambda _: page.go("/segunda")),
                ],
            )
        )

        if page.route == "/segunda":
            page.views.append(
                View(
                    "/segunda",
                    [
                        AppBar(title=Text("Vamos lá"), bgcolor=Colors.SECONDARY_CONTAINER),
                        Text(value=f' Titulo: {input_titulo.value},'
                                   f' Descriçao: {input_descricao.value}, '
                                   f'Categoria: {input_categoria.value},'
                                   f' Autor: {input_autor.value}'),
                    ],
                )
            )
        page.update()

    input_titulo = ft.TextField(label= "Titulo", hint_text="Digite o titulo")
    input_descricao = ft.TextField(label="Descricao", hint_text="Digite a descricao")
    input_categoria = ft.TextField(label="Categoria", hint_text="Digite a categoria")
    input_autor = ft.TextField(label="Autor", hint_text="Digite o autor")

    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = gerencia_rotas
    page.on_view_pop = voltar
    page.go(page.route)


ft.app(main)
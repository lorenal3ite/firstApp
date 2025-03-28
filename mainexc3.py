from cgitb import text
from pydoc import pager

import flet as ft
from flet.core import page


def main(page: ft.Page, txt_resultado=None):
    # config da pagina
    page.title = "Minha Aplicação Flet"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.width = 375
    page.window.height = 667

    # def de funcoes

    def somar(e):
        soma = int(input_numero1.value) + int(input_numero2.value)
        txt_resultado.value = f'{soma}'
        page.update()

    def subtrair(e):
        subtracao = int(input_numero1.value) - int(input_numero2.value)
        txt_resultado.value = f'{subtracao}'
        page.update()

    def multiplicar(e):
        multiplicacao = int(input_numero1.value) * int(input_numero2.value)
        txt_resultado.value = f'{multiplicacao}'
        page.update()

    def divir(e):
        divisao = int(input_numero1.value) / int(input_numero2.value)
        txt_resultado.value = f'{divisao}'
        page.update()

        # criação de componentes

    input_numero1 = ft.TextField(label="Numero", hint_text="digite seu numero")
    input_numero2 = ft.TextField(label="Numero", hint_text="digite seu numero")
    btn_enviar1 = ft.FilledButton(
        text="somar",
        width=page.window.width,
        on_click=somar,
    )
    txt_resultado = ft.Text(value="")

    btn_enviar2 = ft.FilledButton(
        text="subtrair",
        width=page.window.width,
        on_click=subtrair,
    )
    txt_resultado = ft.Text(value="")

    btn_enviar3 = ft.FilledButton(
        text="multiplicar",
        width=page.window.width,
        on_click= multiplicar,
    )
    txt_resultado = ft.Text(value="")

    btn_enviar4 = ft.FilledButton(
        text="dividir",
        width=page.window.width,
        on_click=divir,
    )
    txt_resultado = ft.Text(value="")

    # layout
    page.add(
        ft.Column(
            (
                [input_numero1,
                 input_numero2,
                 btn_enviar1,
                 btn_enviar2,
                 btn_enviar3,
                 btn_enviar4,
                 txt_resultado,

                 ]
            )
        )
    )


ft.app(main)

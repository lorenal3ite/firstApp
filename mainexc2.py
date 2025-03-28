from cgitb import text

import flet as ft
from flet.core import page


def main(page: ft.Page):
    # config da pagina
    page.title = "Minha aplicação flet"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.width = 375
    page.window.height = 667

    # def de funcoes

    def par_ou_impar(e):
        txt_resultado.value = input_numero.value
        numero = int(input_numero.value)
        resultado = numero % 2
        if resultado == 0:
            txt_resultado.value = f"O numero inserido é PAR"
        else:
            txt_resultado.value = f"O numero inserido é IMPAR"
        page.update()


        # criação de componentes


    input_numero = ft.TextField(label="Digite seu numero", hint_text="exemplo: 20 ")
    btn_enviar = ft.FilledButton(
        text="Enviar",
        width=page.window.width,
        on_click=par_ou_impar,
    )
    txt_resultado = ft.Text(value="")

    # layout
    page.add(
        ft.Column(
            (
                input_numero,
                btn_enviar,
                txt_resultado,
            )
        )
    )

ft.app(main)
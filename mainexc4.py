from datetime import datetime
import flet as ft

def main(page: ft.Page, txt_resultado=None):
    # config da pagina
    page.title = "Minha Aplicação Flet"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.width = 375
    page.window.height = 667

    def mostrar_idade(e):
        txt_resultado.value = input_data_nas.value
        data_nascimento = datetime.strptime(txt_resultado.value, "%d/%m/%Y")
        data_atual = datetime.now()
        idade = data_atual.year - data_nascimento.year
        if data_nascimento.month > data_atual.month:
            idade = idade - 1
        if int(idade) >= 10:
            txt_resultado.value = f'Voce tem {idade} anos e é maior de idade'
        else:
            txt_resultado.value = f'Voce tem {idade} anos e é menor de idade'
        page.update()

    input_data_nas = ft.TextField(label="Data de nascimento ", hint_text="Digite a data de nascimento: ")
    btn_enviar = ft.FilledButton(
        text="Enviar",
        width=page.window.width,
        on_click=mostrar_idade,
    )
    txt_resultado = ft.Text(value="")

    # layout
    page.add(
        ft.Column(
            (
                input_data_nas,
                btn_enviar,
                txt_resultado,
            )
        )
    )


ft.app(main)

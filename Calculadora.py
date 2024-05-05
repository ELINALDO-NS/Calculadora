import flet as ft
from flet import colors
botoes = [
    {"Operador": "AC", "Fonte": colors.BLACK, "Fundo": colors.BLUE_GREY_100},
    {"Operador": "±", "Fonte": colors.BLACK, "Fundo": colors.BLUE_GREY_100},
    {"Operador": "%", "Fonte": colors.BLACK, "Fundo": colors.BLUE_GREY_100},
    {"Operador": "/", "Fonte": colors.WHITE, "Fundo": colors.ORANGE},
    {"Operador": "7", "Fonte": colors.WHITE, "Fundo": colors.WHITE24},
    {"Operador": "8", "Fonte": colors.WHITE, "Fundo": colors.WHITE24},
    {"Operador": "9", "Fonte": colors.WHITE, "Fundo": colors.WHITE24},
    {"Operador": "*", "Fonte": colors.WHITE, "Fundo": colors.ORANGE},
    {"Operador": "4", "Fonte": colors.WHITE, "Fundo": colors.WHITE24},
    {"Operador": "5", "Fonte": colors.WHITE, "Fundo": colors.WHITE24},
    {"Operador": "6", "Fonte": colors.WHITE, "Fundo": colors.WHITE24},
    {"Operador": "-", "Fonte": colors.WHITE, "Fundo": colors.ORANGE},
    {"Operador": "1", "Fonte": colors.WHITE, "Fundo": colors.WHITE24},
    {"Operador": "2", "Fonte": colors.WHITE, "Fundo": colors.WHITE24},
    {"Operador": "3", "Fonte": colors.WHITE, "Fundo": colors.WHITE24},
    {"Operador": "+", "Fonte": colors.WHITE, "Fundo": colors.ORANGE},
    {"Operador": "0", "Fonte": colors.WHITE, "Fundo": colors.WHITE24},
    {"Operador": ".", "Fonte": colors.WHITE, "Fundo": colors.WHITE24},
    {"Operador": "=", "Fonte": colors.WHITE, "Fundo": colors.ORANGE},

]


def main(page: ft.Page):
    page.bgcolor = '#000'
    page.window_maximizable = False
    page.window_resizable = False
    page.window_width = 280
    page.window_height = 400
    page.title = 'Calculadora'
    page.window_always_on_top = True

    result = ft.Text(value="0", color=colors.WHITE, size=30)
    def calculate(operador,value_at):
       try:
        value = eval(value_at)
        if  operador == "%":
            value = value / 100
        elif value ==  "±":
            value = -value
       except:
        return "Error"
       return value    




    def select(e):
        value_at = result.value if result.value not in ("0","Error")  else ''
        value = e.control.content.value
        if value.isdigit():
            value = value_at + value
        elif value == "AC":
            value = "0"
        else:
            if value_at and value_at[-1] in ("/", "*", "-", "+", "."):
                value_at = value_at[:-1]
            value = value_at + value
            if value[-1] in ("=", "%", "±"):
                value = calculate(operador=value[-1],value_at=value_at)
        result.value = value
        result.update()
        
    display = ft.Row(
        width=250,
        controls=[result],
        alignment="end"
    )

    btn = [ft.Container(
        content=ft.Text(value=btn["Operador"], color=btn["Fonte"]),
        width=50,
        height=50,
        bgcolor=btn["Fundo"],
        border_radius=100,
        on_click=select,
        alignment=ft.alignment.center
    ) for btn in botoes]

    keybord = ft.Row(
        width=250,
        wrap=True,
        controls=btn,
        alignment="end"
    )

    page.add(display, keybord)


ft.app(target=main)

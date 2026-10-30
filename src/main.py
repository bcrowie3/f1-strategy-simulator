import flet as ft
from constants.colours import GENERAL_COLOURS, TEAM_COLOURS


def main(page: ft.Page):
    page.title = "F1 Strategy Sim"

    page.bgcolor = GENERAL_COLOURS["background"]

    #Ensures that Arial is always a font available and saves is as "mainFont" 
    page.fonts = {
        "mainFont": "fonts/Arial.ttf",
    }

    #Sets Arial as the default font for all page instaces
    page.theme = ft.Theme(
        font_family="mainFont",
    )

    #App Title
    title = ft.Text(
        "F1 Strategy Simulator", 
        size = 64,
        color = GENERAL_COLOURS["tester"]
        )

    page.add(
        ft.Container(
            title,
            alignment=ft.alignment.center,
            padding=20,
            expand=True,
        ),
    )


ft.app(main, assets_dir="assets")

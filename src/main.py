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

    #App title
    title = ft.Text(
        "F1 Strategy Simulator", 
        size = 64,
        color = GENERAL_COLOURS["main_text"]
        )
    
    #"Start" button
    startButton = ft.Button(
        "Start",
        on_click=lambda _: None,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=15),
            text_style=ft.TextStyle(size=18),
            color=GENERAL_COLOURS["main_text"],
            bgcolor={
                ft.ControlState.DEFAULT: GENERAL_COLOURS["overlay"],
                ft.ControlState.PRESSED: ft.Colors.TRANSPARENT
            },
            overlay_color={
                ft.ControlState.DEFAULT: ft.Colors.TRANSPARENT,
                ft.ControlState.HOVERED: GENERAL_COLOURS["nav_button_highlight"],
                ft.ControlState.PRESSED: ft.Colors.TRANSPARENT
            },
            side = ft.BorderSide(
                width=2.0,
                color=GENERAL_COLOURS["nav_button_highlight"],
            ),
            padding=ft.padding.symmetric(
                vertical=15,
                horizontal=20
            )
        ),
    )

    page.add(
        ft.Stack(
            controls=[
                ft.Container(
                    content=title,
                    alignment=ft.alignment.center,
                ),
                ft.Container(
                    content=startButton,
                    alignment=ft.alignment.bottom_right,
                    padding=10,
                )
            ],
            expand=True
        )      
    )


ft.app(main, assets_dir="assets")

import flet as ft
from constants.colours import GENERAL_COLOURS

def homePage(page: ft.Page):
    #App title
    title=ft.Text(
        "F1 Strategy Simulator", 
        size=64,
        color=GENERAL_COLOURS["main text"]
        )
    
    #"Start" button
    startButton=ft.Button(
        "Start",
        key="start",
        on_click=lambda _: page.navigate("/setup"),
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=15),
            text_style=ft.TextStyle(size=18),
            color=GENERAL_COLOURS["main text"],
            bgcolor={
                ft.ControlState.DEFAULT: GENERAL_COLOURS["overlay"],
                ft.ControlState.PRESSED: ft.Colors.TRANSPARENT
            },
            overlay_color={
                ft.ControlState.DEFAULT: ft.Colors.TRANSPARENT,
                ft.ControlState.HOVERED: GENERAL_COLOURS["nav button highlight"],
                ft.ControlState.PRESSED: ft.Colors.TRANSPARENT
            },
            side=ft.BorderSide(
                width=2.0,
                color=GENERAL_COLOURS["nav button highlight"],
            ),
            padding=ft.Padding.symmetric(
                vertical=15,
                horizontal=20
            )
        ),
    )

    return ft.View(
        route="/",
        bgcolor=GENERAL_COLOURS["background"],
        controls=[
            ft.Stack(
                controls=[
                    ft.Container(
                        content=title,
                        alignment=ft.Alignment.CENTER,
                    ),
                    ft.Container(
                        content=startButton,
                        alignment=ft.Alignment.BOTTOM_RIGHT,
                        padding=10,
                    )
                ],
                expand=True
            )      
        ]
    )
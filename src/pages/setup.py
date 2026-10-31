import flet as ft
from constants.colours import GENERAL_COLOURS, TEAM_COLOURS

def setupPage(page: ft.Page):
    #Page title
    title = ft.Text(
        "Page 2 tester", 
        size = 64,
        color = GENERAL_COLOURS["main text"]
        )
    
    qualifyingButton = ft.Button(
        "Qualifying",
        on_click=lambda _: None,
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
            side = ft.BorderSide(
                width=2.0,
                color=GENERAL_COLOURS["nav button highlight"],
            ),
            padding=ft.padding.symmetric(
                vertical=15,
                horizontal=20
            )
        ),
    )

    return ft.View(
        route="/setup",
        bgcolor=GENERAL_COLOURS["background"],
        controls=[
            ft.Stack(
                controls=[
                    ft.Container(
                        content=title,
                        alignment=ft.alignment.center,
                    ),
                    ft.Container(
                        content=qualifyingButton,
                        alignment=ft.alignment.bottom_right,
                        padding=10,
                    )
                ],
                expand=True
            )      
        ]
    )
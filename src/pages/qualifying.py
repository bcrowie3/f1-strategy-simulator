import flet as ft
from constants.colours import GENERAL_COLOURS, TEAM_COLOURS
from constants.drivers import DRIVERS

def qualifyingPage(page: ft.Page):

    #Page title
    flag = ft.Image(
        src="images/chequered_flag.png",
        key="qualis chequered flag",
        width=300,
        height=65,
        fit=ft.BoxFit.COVER
        )
    
    #Button to navigate to the next page
    qualifyingButton = ft.Button(
        "The Grid",
        key="the grid",
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
        route="/qualifying",
        bgcolor=GENERAL_COLOURS["background"],
        controls=[
            ft.Stack(
                controls=[
                    ft.Container(
                        content=flag,
                        alignment=ft.Alignment.TOP_CENTER,
                    ),
                    ft.Container(
                        content=qualifyingButton,
                        alignment=ft.Alignment.BOTTOM_RIGHT,
                        padding=10,
                    )
                ],
                expand=True
            )    
        ],
        padding=0
    )
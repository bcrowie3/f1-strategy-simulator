import flet as ft
from constants.colours import GENERAL_COLOURS, TEAM_COLOURS

def setupPage(page: ft.Page):
    #Page title
    title = ft.Text(
        "Select a driver, track, and difficulty", 
        size = 44,
        color = GENERAL_COLOURS["main text"]
        )
    
    #Button to navigate to the next page
    qualifyingButton=ft.Button(
        "Qualifying",
        key="qualifying",
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

    #Button to navigate back to the home page
    backButton=ft.IconButton(
        icon=ft.Icons.ARROW_BACK_IOS,
        key="back",
        on_click=lambda _: page.navigate("/"),
        style=ft.ButtonStyle(
            icon_size=40,
            bgcolor={
                ft.ControlState.DEFAULT: ft.Colors.TRANSPARENT,
            },
            overlay_color={
                ft.ControlState.DEFAULT: ft.Colors.TRANSPARENT,
                ft.ControlState.PRESSED: ft.Colors.TRANSPARENT
            },
            icon_color={
                ft.ControlState.DEFAULT: GENERAL_COLOURS["overlay"],
                ft.ControlState.HOVERED: GENERAL_COLOURS["main text"],
                ft.ControlState.PRESSED: GENERAL_COLOURS["tester"]
            },
            
            padding=0,
        )
    )

    return ft.View(
        route="/setup",
        bgcolor=GENERAL_COLOURS["background"],

        #Header with the title and back button
        appbar = ft.AppBar(
            leading=ft.Container(
                content=backButton,
                padding=ft.Padding(
                    left=10,
                    right=0,
                    top=0,
                    bottom=0
                )
            ),
            leading_width=42,
            title=title,
            center_title=True,
            bgcolor=GENERAL_COLOURS["background"],
        ),
        controls=[
            ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Container(
                                content=ft.Text("placeholder"),
                                alignment=ft.Alignment.CENTER,
                                expand=True
                            )
                        ],
                        tight=True,
                        
                    ),
                    ft.Container(
                        content=qualifyingButton,
                        alignment=ft.Alignment.BOTTOM_RIGHT,
                        padding=10,
                        expand=True
                    )
                ],
                expand=True
            )      
        ]
    )
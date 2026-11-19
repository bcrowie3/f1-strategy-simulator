import flet as ft
from constants.colours import GENERAL_COLOURS, TEAM_COLOURS
from constants.drivers import DRIVERS

def qualifyingPage(page: ft.Page):

    def pause():
        pauseMenu.visible = True
        page.update
    
    def resume():
        pauseMenu.visible = False
        page.update
    
    def quit():
        page.overlay.remove(pauseMenu)
        page.update
        page.navigate("/")
    
    def toGrid():
        page.overlay.remove(pauseMenu)
        page.update
        page.navigate("/grid")

    #Page title
    flag = ft.Image(
        src="images/chequered_flag.png",
        key="qualis chequered flag",
        width=300,
        height=65,
        fit=ft.BoxFit.COVER
        )
    
    #Button to navigate to the next page
    gridButton = ft.Button(
        "The Grid",
        key="the grid",
        on_click=lambda _: toGrid(),
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

    pauseMenu = ft.Container(
        key="quali paused",
        visible=False,

        #Pulls the container to each edge
        top=0,
        bottom=0,
        left=0,
        right=0,

        bgcolor=GENERAL_COLOURS["paused screen"],
        blur=6,
        alignment=ft.Alignment.CENTER,

        content=ft.Column(
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
            
            controls=[
                ft.Text(
                    "Paused",
                    size=38,
                    color=GENERAL_COLOURS["main text"]
                ),
                ft.TextButton(
                    content="Resume",
                    key="quali resume",
                    on_click=lambda _: resume(),
                    style=ft.ButtonStyle(
                        color={
                            ft.ControlState.DEFAULT: GENERAL_COLOURS["main text"],
                            ft.ControlState.HOVERED: f"#66{GENERAL_COLOURS['main text'][1:]}"
                        },
                        overlay_color=ft.Colors.TRANSPARENT,
                        text_style=ft.TextStyle(size=28),
                    )
                ),
                ft.TextButton(
                    content="Quit",
                    key="quali quit",
                    on_click=lambda _: quit(),
                    style=ft.ButtonStyle(
                        color={
                            ft.ControlState.DEFAULT: GENERAL_COLOURS["main text"],
                            ft.ControlState.HOVERED: f"#66{GENERAL_COLOURS['main text'][1:]}"
                        },
                        overlay_color=ft.Colors.TRANSPARENT,
                        text_style=ft.TextStyle(size=28),
                    )
                )
            ]
        )
    )

    pauseButton = ft.IconButton(
        icon=ft.Icons.PAUSE,
        key="quali pause",
        on_click=lambda _: pause(),
        width=40,
        height=40,
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

    page.overlay.append(pauseMenu)

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
                        content=gridButton,
                        bottom=10,
                        right=10
                    ), 
                    ft.Container(
                        content=pauseButton,
                        bottom=2
                    )
                ],
                expand=True,
                alignment=ft.Alignment.CENTER
            )    
        ],
        padding=0
    )
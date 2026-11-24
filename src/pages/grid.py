import flet as ft
from constants.colours import GENERAL_COLOURS, TEAM_COLOURS
from constants.drivers import DRIVERS
from constants.tracks import TRACKS
import backend.qualis as qualis

def gridPage(page: ft.Page):

    def pause():
        pauseMenu.visible = True
        page.update
    
    def resume():
        pauseMenu.visible = False
        page.update
    
    def quit():
        page.overlay.remove(pauseMenu)
        page.update()
        qualis.clear_selections()
        qualis.clear_positions()
        page.navigate("/")
    
    def to_driver_briefing():
        page.overlay.remove(pauseMenu)
        page.navigate("/grid") #ADD ROUTE OF DRIVER BRIEFING

    #Page title
    title = ft.Text(
        "The Grid", 
        size=44,
        color=GENERAL_COLOURS["main text"]
        )
    
    #"Start" button
    driverBriefingButton = ft.Button(
        "Driver Briefing",
        key="driver briefing",
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
            },
            
            padding=0,
        )
    )

    #First part of the heading for the positions table
    headingA = ft.Text(
        "F1", 
        size=32,
        color=GENERAL_COLOURS["main text"]
    )

    #Second part of the heading for the positions table
    headingB = ft.Text(
        "Strategy", 
        size=24,
        color=GENERAL_COLOURS["main text"]
    )

    #First part of the time for the positions table
    subheading = ft.Text(
        "Qualifying Results", 
        size=16,
        color=GENERAL_COLOURS["main text"]
    )

    rowsOfResults = [
        ft.Row(
            spacing=0,
            controls=[
                ft.Text(
                    f" {place}" if place < 10 else f"{place}",
                    width=25,   #Sets a static width allowing all
                    size=16,
                    color=GENERAL_COLOURS["main text"]
                ),
                ft.Text(
                    data["team"][:3].capitalize(),
                    width=40,
                    size=14,
                    color=TEAM_COLOURS[data["team"]]
                ),
                ft.Text(
                    DRIVERS[data["driver"]]["surname"][:3].upper(),
                    width=55,
                    size=16,
                    color=GENERAL_COLOURS["main text"]
                ),
                ft.Text(
                    f"{data["formatted time"]}",
                    size=16,
                    color=GENERAL_COLOURS["main text"]
                )
            ]
        )
        for place, data in qualis.positions.items()
    ]
    
    #Odd grid places
    oddGrid = [
        ft.Container(
            alignment=ft.Alignment.BOTTOM_CENTER,
            width=150,
            height=30,
            padding=ft.Padding.only(
                left=5,
                right=5,
                top=5,
                bottom=0
            ),
            border=ft.Border.only(
                left=ft.BorderSide(
                    width=4.0,
                    color=GENERAL_COLOURS["main text"]
                ),
                right=ft.BorderSide(
                    width=4.0,
                    color=GENERAL_COLOURS["main text"]
                ),
                top=ft.BorderSide(
                    width=4.0,
                    color=GENERAL_COLOURS["main text"]
                )
            ),
            content=ft.Text(
                DRIVERS[data["driver"]]["surname"][:3].upper(),
                size=20,
                weight=ft.FontWeight.BOLD,
                color=TEAM_COLOURS[data["team"]]
            ),
        )
        for position, data in qualis.positions.items()
        if position % 2 != 0
    ]

    #Even grid places
    evenGrid = [
        ft.Container(
            alignment=ft.Alignment.BOTTOM_CENTER,
            width=150,
            height=30,
            padding=ft.Padding.only(
                left=5,
                right=5,
                top=5,
                bottom=0
            ),
            border=ft.Border.only(
                left=ft.BorderSide(
                    width=4.0,
                    color=GENERAL_COLOURS["main text"]
                ),
                right=ft.BorderSide(
                    width=4.0,
                    color=GENERAL_COLOURS["main text"]
                ),
                top=ft.BorderSide(
                    width=4.0,
                    color=GENERAL_COLOURS["main text"]
                )
            ),
            content=ft.Text(
                DRIVERS[data["driver"]]["surname"][:3].upper(),
                size=20,
                weight=ft.FontWeight.BOLD,
                color=TEAM_COLOURS[data["team"]]
            ),
        )
        for position, data in qualis.positions.items()
        if position % 2 == 0
    ]

    columnOffset = ft.Container(
        width=100,
        height=1,
    )

    #Grid columns
    if TRACKS[qualis.userTrack]["pole side"] == "left":
        startingGrid = ft.Container(
            ft.Row(
                spacing=75,
                controls=[
                    ft.Column(
                        spacing=25,
                        controls=[*oddGrid]
                    ),
                    ft.Column(
                        spacing=25,
                        controls=[
                            columnOffset,
                            *evenGrid
                        ]
                    )  
                ]
            ),
            width=375,
            top=75,
        )
    else:
         startingGrid = ft.Container(
            ft.Row(
                spacing=75,
                controls=[
                    ft.Column(
                        spacing=25,
                        controls=[
                            columnOffset,
                            *evenGrid
                        ]
                    ),
                    ft.Column(
                        spacing=25,
                        controls=[*oddGrid]
                    )  
                ]
            ),
            width=375,
            top=75,
        )

    page.overlay.append(pauseMenu)

    return ft.View(
        route="/grid",
        bgcolor=GENERAL_COLOURS["background"],
        padding=0,
        controls=[
            ft.Stack(
                expand=True,
                alignment=ft.Alignment.CENTER,
                controls=[
                    ft.Container(
                        content=title,
                        alignment=ft.Alignment.TOP_CENTER,
                    ),
                    ft.Container(
                        content=driverBriefingButton,
                        bottom=10,
                        right=10
                    ),
                    ft.Container(
                        content=pauseButton,
                        bottom=2
                    ),

                    #Positions table
                    ft.Column(
                        left=0,
                        top=0,
                        spacing=0,
                        controls=[
                            ft.Container(
                                width=200,
                                padding=10,
                                border=ft.Border.only(
                                    right=ft.BorderSide(
                                        width=2.0,
                                        color=GENERAL_COLOURS["overlay"]
                                    ),
                                    bottom=ft.BorderSide(
                                        width=2.0,
                                        color=GENERAL_COLOURS["overlay"]
                                    )
                                ),
                                content=ft.Column(
                                    spacing=5,
                                    controls=[
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            vertical_alignment=ft.CrossAxisAlignment.BASELINE,
                                            spacing=8,
                                            controls=[
                                                headingA,
                                                headingB
                                            ]
                                        ),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            spacing=5,
                                            controls=[
                                                subheading,
                                                
                                            ]
                                        )
                                    ]
                                )
                            ),
                            ft.Container(
                                width=200,
                                padding=3,
                                border=ft.Border.only(
                                    right=ft.BorderSide(
                                        width=2.0,
                                        color=GENERAL_COLOURS["overlay"]
                                    ),
                                    bottom=ft.BorderSide(
                                        width=2.0,
                                        color=GENERAL_COLOURS["overlay"]
                                    )
                                ),
                                content=ft.Column(
                                    spacing=3,
                                    controls=[
                                        *rowsOfResults
                                    ]
                                )
                            )
                        ],
                    ),

                    #Starting Grid
                    startingGrid
                ],
            )      
        ]
    )
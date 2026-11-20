import flet as ft
from constants.colours import GENERAL_COLOURS, TEAM_COLOURS, TIMING_COLOURS
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
        "strategy", 
        size=24,
        color=GENERAL_COLOURS["main text"]
    )

    #First part of the time for the positions table
    q3 = ft.Text(
        "Q3", 
        size=16,
        color=GENERAL_COLOURS["main text"]
    )

    #Second part of the time for the positions table
    timer = ft.Text(
        "0:00",
        size=16,
        color=TIMING_COLOURS["quali end"]
    )

    #Row for p1 - all row logic will be amended to be fed data from backend 
    p1 = ft.Row(
        spacing=0,
        controls=[
            ft.Text(
                " 1",
                width=25,   #Sets a static width allowing all
                size=16,
                color=GENERAL_COLOURS["main text"]
            ),
            ft.Text(
                DRIVERS[3]["team"][:3].capitalize(),
                width=40,
                size=14,
                color=TEAM_COLOURS[DRIVERS[3]["team"]]
            ),
            ft.Text(
                DRIVERS[3]["surname"][:3].upper(),
                width=55,
                size=16,
                color=GENERAL_COLOURS["main text"]
            ),
            ft.Text(
                "-0.047",
                size=16,
                color=GENERAL_COLOURS["main text"]
            )
        ]
    )

    #Row for P2
    p2 = ft.Row(
        spacing=0,
        controls=[
            ft.Text(
                " 2",
                width=25,
                size=16,
                color=GENERAL_COLOURS["main text"]
            ),
            ft.Text(
                DRIVERS[44]["team"][:3].capitalize(),
                width=40,
                size=14,
                color=TEAM_COLOURS[DRIVERS[44]["team"]]
            ),
            ft.Text(
                DRIVERS[44]["surname"][:3].upper(),
                width=55,
                size=16,
                color=GENERAL_COLOURS["main text"]
            ),
            ft.Text(
                "1:34:067",
                size=16,
                color=GENERAL_COLOURS["main text"]
            )
        ]
    )

    #Row for P3
    p3 = ft.Row(
        spacing=0,
        controls=[
            ft.Text(
                " 3",
                width=25,
                size=16,
                color=GENERAL_COLOURS["main text"]
            ),
            ft.Text(
                DRIVERS[16]["team"][:3].capitalize(),
                width=40,
                size=14,
                color=TEAM_COLOURS[DRIVERS[16]["team"]]
            ),
            ft.Text(
                DRIVERS[16]["surname"][:3].upper(),
                width=55,
                size=16,
                color=GENERAL_COLOURS["main text"]
            ),
            ft.Text(
                "+0.093",
                size=16,
                color=GENERAL_COLOURS["main text"]
            )
        ]
    )

    #Row for P4
    p4 = ft.Row(
        spacing=0,
        controls=[
            ft.Text(
                " 4",
                width=25,
                size=16,
                color=GENERAL_COLOURS["main text"]
            ),
        ]
    )

    #Row for P5
    p5 = ft.Row(
        spacing=0,
        controls=[
            ft.Text(
                " 5",
                width=25,
                size=16,
                color=GENERAL_COLOURS["main text"]
            ),
        ]
    )

    #Row for P6
    p6 = ft.Row(
        spacing=0,
        controls=[
            ft.Text(
                " 6",
                width=25,
                size=16,
                color=GENERAL_COLOURS["main text"]
            ),
        ]
    )

    #Row for P7
    p7 = ft.Row(
        spacing=0,
        controls=[
            ft.Text(
                " 7",
                width=25,
                size=16,
                color=GENERAL_COLOURS["main text"]
            ),
        ]
    )

    #Row for P8
    p8 = ft.Row(
        spacing=0,
        controls=[
            ft.Text(
                " 8",
                width=25,
                size=16,
                color=GENERAL_COLOURS["main text"]
            ),
        ]
    )

    #Row for P9
    p9 = ft.Row(
        spacing=0,
        controls=[
            ft.Text(
                " 9",
                width=25,
                size=16,
                color=GENERAL_COLOURS["main text"]
            ),
        ]
    )

    #Row for P10
    p10 = ft.Row(
        spacing=0,
        controls=[
            ft.Text(
                "10",
                width=25,
                size=16,
                color=GENERAL_COLOURS["main text"]
            ),
        ]
    )

    #Row for P11
    p11 = ft.Row(
        spacing=0,
        controls=[
            ft.Text(
                "11",
                width=25,
                size=16,
                color=GENERAL_COLOURS["main text"]
            ),
        ]
    )

    #Row for P12
    p12 = ft.Row(
        spacing=0,
        controls=[
            ft.Text(
                "12",
                width=25,
                size=16,
                color=GENERAL_COLOURS["main text"]
            ),
        ]
    )

    #Row for P13
    p13 = ft.Row(
        spacing=0,
        controls=[
            ft.Text(
                "13",
                width=25,
                size=16,
                color=GENERAL_COLOURS["main text"]
            ),
        ]
    )

    #Row for P14
    p14 = ft.Row(
        spacing=0,
        controls=[
            ft.Text(
                "14",
                width=25,
                size=16,
                color=GENERAL_COLOURS["main text"]
            ),
        ]
    )

    #Row for P15
    p15 = ft.Row(
        spacing=0,
        controls=[
            ft.Text(
                "15",
                width=25,
                size=16,
                color=GENERAL_COLOURS["main text"]
            ),
        ]
    )

    #Row for P16
    p16 = ft.Row(
        spacing=0,
        controls=[
            ft.Text(
                "16",
                width=25,
                size=16,
                color=GENERAL_COLOURS["main text"]
            ),
        ]
    )

    #Row for P17
    p17 = ft.Row(
        spacing=0,
        controls=[
            ft.Text(
                "17",
                width=25,
                size=16,
                color=GENERAL_COLOURS["main text"]
            ),
        ]
    )

    #Row for P18
    p18 = ft.Row(
        spacing=0,
        controls=[
            ft.Text(
                "18",
                width=25,
                size=16,
                color=GENERAL_COLOURS["main text"]
            ),
        ]
    )

    #Row for P19
    p19 = ft.Row(
        spacing=0,
        controls=[
            ft.Text(
                "19",
                width=25,
                size=16,
                color=GENERAL_COLOURS["main text"]
            ),
        ]
    )

    #Row for P20
    p20 = ft.Row(
        spacing=0,
        controls=[
            ft.Text(
                "20",
                width=25,
                size=16,
                color=GENERAL_COLOURS["main text"]
            ),
        ]
    )

    #Row for P21
    p21 = ft.Row(
        spacing=0,
        controls=[
            ft.Text(
                "21",
                width=25,
                size=16,
                color=GENERAL_COLOURS["main text"]
            ),
        ]
    )

    #Row for P22
    p22 = ft.Row(
        spacing=0,
        controls=[
            ft.Text(
                "22",
                width=25,
                size=16,
                color=GENERAL_COLOURS["main text"]
            ),
        ]
    )

    page.overlay.append(pauseMenu)

    return ft.View(
        route="/qualifying",
        bgcolor=GENERAL_COLOURS["background"],
        padding=0,
        controls=[
            ft.Stack(
                expand=True,
                alignment=ft.Alignment.CENTER,
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
                                                q3,
                                                timer
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
                                        p1,
                                        p2,
                                        p3,
                                        p4,
                                        p5,
                                        p6,
                                        p7,
                                        p8,
                                        p9,
                                        p10,
                                        p11,
                                        p12,
                                        p13,
                                        p14,
                                        p15,
                                        p16,
                                        p17,
                                        p18,
                                        p19,
                                        p20,
                                        p21,
                                        p22
                                    ]
                                )
                            )
                        ],
                    )
                ], 
            )    
        ],
    )
import flet as ft
from constants.colours import GENERAL_COLOURS, TEAM_COLOURS
from constants.drivers import DRIVERS
from constants.tracks import TRACKS
from constants.difficulty import DIFFICULTY_LEVELS
import backend.qualis as qualis
import asyncio

def setupPage(page: ft.Page):

    #Underlines the selected driver and clears past selection if required
    def highlight_selected_driver():
        for driver in driverNames:
            if driver.key == qualis.userDriver:
                driver.style = driver.style.copy(
                    text_style=driver.style.text_style.copy(
                        decoration=ft.TextDecoration.UNDERLINE
                    )
                )
            else:
                driver.style = driver.style.copy(
                    text_style=driver.style.text_style.copy(
                        decoration=ft.TextDecoration.NONE
                    )
                )
    
    #Underlines the selected track and clears past selection if required
    def highlight_selected_track():
        for track in trackNames:
            if track.key == qualis.userTrack:
                track.style = track.style.copy(
                    text_style=track.style.text_style.copy(
                        decoration=ft.TextDecoration.UNDERLINE
                    )
                )
            else:
                track.style = track.style.copy(
                    text_style=track.style.text_style.copy(
                        decoration=ft.TextDecoration.NONE
                    )
                )

    #Underlines the selected difficulty and clears past selection if required
    def highlight_selected_difficulty():
        for difficulty in diffLevels:
            if difficulty.key == qualis.userDifficulty:
                difficulty.style = difficulty.style.copy(
                    text_style=difficulty.style.text_style.copy(
                        decoration=ft.TextDecoration.UNDERLINE
                    )
                )
            else:
                difficulty.style = difficulty.style.copy(
                    text_style=difficulty.style.text_style.copy(
                        decoration=ft.TextDecoration.NONE
                    )
                )
    
    #Selects (and highlights) the driver/unselects if already selected
    def select_driver(selectedDr: int):
        if not qualis.userDriver == selectedDr:
            qualis.userDriver = selectedDr
        else:
            qualis.userDriver = None
        highlight_selected_driver()
        update_instructionLine()

    #Selects (and highlights) the track/unselects if already selected
    def select_track(selectedTr: str):
        if not qualis.userTrack == selectedTr:
            qualis.userTrack = selectedTr
        else:
            qualis.userTrack = None
        highlight_selected_track()
        update_instructionLine()

    #Selects (and highlights) the difficulty/unselects if already selected
    def select_difficulty(selectedDi: str):
        if not qualis.userDifficulty == selectedDi:
            qualis.userDifficulty = selectedDi
        else:
            qualis.userDifficulty = None
        highlight_selected_difficulty()
        update_instructionLine()
    
    def generate_instructions():
        instructions = "Before proceeding, please select a"

        if qualis.userDriver is None and qualis.userTrack is not None and qualis.userDifficulty is not None:
            instructions += " driver."

        if qualis.userDriver is not None and qualis.userTrack is None and qualis.userDifficulty is not None:
            instructions += " track."

        if qualis.userDriver is not None and qualis.userTrack is not None and qualis.userDifficulty is None:
            instructions += " difficulty."

        if qualis.userDriver is None and qualis.userTrack is None and qualis.userDifficulty is not None:
            instructions += " driver and track."

        if qualis.userDriver is None and qualis.userTrack is not None and qualis.userDifficulty is None:
            instructions += " driver and difficulty."
        
        if qualis.userDriver is not None and qualis.userTrack is None and qualis.userDifficulty is None:
            instructions += " track and difficulty."

        if qualis.userDriver is None and qualis.userTrack is None and qualis.userDifficulty is None:
            instructions += " driver, track, and difficulty."
        
        if qualis.userDriver is not None and qualis.userTrack is not None and qualis.userDifficulty is not None:
            instructions = "All necessary selections have been satisfied."
        
        return instructions
    
    def update_instructionLine():
        instructionLine.value = generate_instructions()
        page.update()

    def back_to_home():
        qualis.clear_selections()
        page.navigate("/")

     
    async def to_qualifying():
        if qualis.userDriver is None or qualis.userTrack is None or qualis.userDifficulty is None:
            #Stores the starting colour of each heading
            driverStartingColor = driverHeading.color
            trackStartingColor = driverHeading.color
            difficultyStartingColor = difficultyHeading.color

            #If a section has no selection the heading colour is changed 
            if qualis.userDriver is None:
                driverHeading.color = GENERAL_COLOURS["error"]
            if qualis.userTrack is None:
                trackHeading.color = GENERAL_COLOURS["error"]
            if qualis.userDifficulty is None:
                difficultyHeading.color = GENERAL_COLOURS["error"]

            #Updates UI for error colouring and waits for 3 seconds
            page.update()
            await asyncio.sleep(3)

            #Ensures any changed heading colours are reverted to the original
            driverHeading.color = driverStartingColor
            trackHeading.color = trackStartingColor
            difficultyHeading.color = difficultyStartingColor
            page.update()
            
            return
        
        else:
            qualis.hot_laps()
            page.navigate("/qualifying")

    #Page title
    title = ft.Text(
        "Race Setup", 
        size=44,
        color=GENERAL_COLOURS["main text"]
        )
    
    #Button to navigate to the next page
    qualifyingButton = ft.Button(
        "Qualifying",
        key="qualifying",
        on_click=to_qualifying,
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
    backButton = ft.IconButton(
        icon=ft.Icons.ARROW_BACK_IOS,
        key="back",
        on_click=lambda _: back_to_home(),
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

    #Header with the title and back button
    appBar = ft.AppBar(
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

        #Stops the appbar from reacting to content scrolling below it
        elevation=0,
        elevation_on_scroll=0
    )

    #Driver heading 
    driverHeading = ft.Text(
        "Driver:", 
        size=38,
        color=GENERAL_COLOURS["main text"]
        )
    
    #Track heading 
    trackHeading = ft.Text(
        "Track:", 
        size=38,
        color=GENERAL_COLOURS["main text"]
        )
    
    #Difficulty heading 
    difficultyHeading = ft.Text(
        "Difficulty:", 
        size=38,
        color=GENERAL_COLOURS["main text"]
        )

    #List of driver buttons
    driverNames = [
        ft.TextButton(
            content=f"{driver["forename"][0].upper()}. {driver["surname"].capitalize()}",
            key=number,
            on_click=lambda _, driverNumber=number: select_driver(driverNumber),
            style=ft.ButtonStyle(
                color={
                    ft.ControlState.DEFAULT: TEAM_COLOURS[driver["team"]],
                    ft.ControlState.HOVERED: f"#66{TEAM_COLOURS[driver["team"]][1:]}"
                },
                overlay_color=ft.Colors.TRANSPARENT,
                text_style=ft.TextStyle(size=28),
            )
        )
        for number, driver in DRIVERS.items()
    ]

    #List of track buttons
    trackNames = [
        ft.TextButton(
            content=f"{name} ({track["country"]})",
            key=name,
            on_click=lambda _, trackName=name: select_track(trackName),
            style=ft.ButtonStyle(
                color={
                    ft.ControlState.DEFAULT: GENERAL_COLOURS["main text"],
                    ft.ControlState.HOVERED: f"#66{GENERAL_COLOURS['main text'][1:]}"
                },
                overlay_color=ft.Colors.TRANSPARENT,
                text_style=ft.TextStyle(size=28)
            )
        )
        for name, track in TRACKS.items()
    ]

    #List of difficulty level buttons
    diffLevels = [
        ft.TextButton(
            content=level,
            key=level,
            on_click=lambda _, difficulty=level: select_difficulty(difficulty),
            style=ft.ButtonStyle(
                color={
                    ft.ControlState.DEFAULT: GENERAL_COLOURS["main text"],
                    ft.ControlState.HOVERED: f"#66{GENERAL_COLOURS['main text'][1:]}"
                },
                overlay_color=ft.Colors.TRANSPARENT,
                text_style=ft.TextStyle(size=28)
            )
        )
        for level in DIFFICULTY_LEVELS
    ]

    instructionLine = ft.Text(
        generate_instructions(), 
        size=20,
        color=GENERAL_COLOURS["main text"]
    )

    return ft.View(
        route="/setup",
        bgcolor=GENERAL_COLOURS["background"],
        appbar=appBar,
        controls=[
            #Instruction line 
            ft.Row(
                instructionLine
            ),

            #Column headings
            ft.Row(
                spacing=10,
                controls=[
                    #Driver heading
                    ft.Column(
                        driverHeading,
                        expand=1,
                    ),
                    #Track heading
                    ft.Column(
                        trackHeading,
                        expand=2,   
                    ),
                    #Difficulty heading
                    ft.Column(
                        difficultyHeading,
                        expand=1,   
                    ),
                ],
            ),

            #Three columns with setup options
            ft.Row(
                expand=True,
                spacing=10,
                controls=[
                    #Driver options
                    ft.Column(
                        controls=[
                            *driverNames
                        ],
                        scroll=ft.ScrollMode.AUTO,
                        expand=1,
                    ),
                    #Track options
                    ft.Column(
                        controls=[
                            *trackNames
                        ],
                        expand=2,   
                    ),
                    #Difficulty options
                    ft.Column(
                        controls=[
                            *diffLevels,
                        ],
                        expand=1,   
                    ),
                ],
            ),
            #Qualifying button
            ft.Container(
                    content=qualifyingButton,
                    alignment=ft.Alignment.BOTTOM_RIGHT,
                    padding=0
            )
        ]
    )
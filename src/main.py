import flet as ft
from constants.colours import GENERAL_COLOURS
from pages.home import homePage
from pages.setup import setupPage
from pages.qualifying import qualifyingPage
from pages.grid import gridPage


def main(page: ft.Page):
    page.title="F1 Strategy Sim"
    page.bgcolor=GENERAL_COLOURS["background"]

    #Saving Arial and setting it as the default font
    page.fonts={"mainFont": "fonts/Arial.ttf"}
    page.theme=ft.Theme(font_family="mainFont")

    #Handles page routing
    def navigate(e=None):
        page.views.clear()

        page.views.append(homePage(page))

        if page.route == "/setup":
            page.views.append(setupPage(page))
        
        if page.route == "/qualifying":
            page.views.append(qualifyingPage(page))
        
        if page.route == "/grid":
            page.views.append(gridPage(page))

        #Refreshes the view
        page.update()

    #If a route change is called the navigate function is called
    page.on_route_change = navigate
    
    #Opens app on the set home page
    navigate()


ft.run(main, assets_dir="assets")

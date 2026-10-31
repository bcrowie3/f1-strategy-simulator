import flet as ft
from constants.colours import GENERAL_COLOURS
from pages.home import homePage
from pages.setup import setupPage


def main(page: ft.Page):
    page.title = "F1 Strategy Sim"
    page.bgcolor = GENERAL_COLOURS["background"]

    #Saving Arial and setting it as the default font
    page.fonts = {"mainFont": "fonts/Arial.ttf"}
    page.theme = ft.Theme(font_family="mainFont")

    #Handles page routing
    def navigate(route):
        if page.route == "/":
            page.views.append(homePage(page))

        elif page.route == "/setup":
            page.views.append(setupPage(page))

        #Refreshes the view
        page.update()

    #If a route change is called the navigate function is called
    page.on_route_change = navigate
    
    #Opens app on the set home page
    page.go("/")


ft.app(main, assets_dir="assets")

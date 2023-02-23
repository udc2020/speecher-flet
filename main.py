from flet import *
from src.app import App



def main(page: Page):

    # App Configs
    page.window_center = True
    page.window_title_bar_hidden = True
    page.padding = 10
    page.title = "Speach-er"
    page.bgcolor = "white"
    page.window_width = 350
    page.window_resizable = False
    page.theme_mode = ThemeMode.LIGHT
    page.window_maximized = False

    # Main App
    main_app = App(page=page)

    # Append & make App as root widget
    page.add(main_app)


if '__main__' == __name__:
    app(main)

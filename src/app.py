from flet import *
from components.DropdownWidget import DropDownWidget

from models.speech import SpeechToText


class App(UserControl):
    list_gender: list[str]
    list_speeds: list[str]
    dropdown_gender: None
    dropdown_speed: None
    text_area: None
    gender_index: int
    speed_index: int

    def __init__(self, page):
        super().__init__()
        # Control main Page
        self.page = page

        # Lists
        self.list_gender = ["Male", "Female"]
        self.list_speeds = ["Slow", "Normal", "Fast"]

        self.dropdown_gender = None
        self.dropdown_speed = None
        self.text_area = None

        # gender = man
        self.gender_index = 0

        # speed = normal
        self.speed_index = 1

        # Floating Action Bar
        self.page.floating_action_button = FloatingActionButton(
            icon=icons.PLAY_ARROW,
            bgcolor=colors.BLUE,
            on_click=self.convert
        )

    def convert(self, e):
        SpeechToText().convert(
            self.text_area.value,
            self.gender_index,
            self.speed_index
        )

    def close_app(self, e):
        # Close App
        self.page.window_close()

    def select_gender(self, e):
        # Select Gender
        match (self.dropdown_gender.get_value()):
            case "Male":  self.gender_index = 0
            case "Female":  self.gender_index = 1
            case _: self.gender_index = 1

    def select_speed(self, e):
        # Select Speed
        match (self.dropdown_speeds.get_value()):
            case "Slow":  self.speed_index = 0
            case "Normal":  self.speed_index = 1
            case "Fast":  self.speed_index = 2
            case _: self.speed_index = 1

    def build(self):
        # add refrence of dropdowns
        self.dropdown_gender = DropDownWidget(
            self.list_gender,
            "Gender",
            self.select_gender
        )

        self.dropdown_speeds = DropDownWidget(
            self.list_speeds,
            "Speed",
            self.select_speed
        )

        # get text value from text field
        self.text_area = TextField(
            hint_text="Put Your Text Here",
            expand=True,
            max_lines=18,
            min_lines=12,
            text_style=TextStyle(
                size=20
            )

        )
        return WindowDragArea(Column(
            controls=[
                Row(
                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        Text('Speach-er', color=colors.BLACK, size=30),
                        IconButton(
                            bgcolor=colors.RED,
                            icon=icons.CLOSE,
                            icon_color="white",
                            on_click=self.close_app,
                            icon_size=12

                        )
                    ]
                ),
                Row(
                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        Container(
                            width=150,
                            bgcolor="white",
                            padding=20,
                            content=self.dropdown_gender
                        ),
                        Container(
                            width=150,
                            padding=20,
                            bgcolor="white",
                            content=self.dropdown_speeds
                        )
                    ]),
                Row(
                    controls=[

                        self.text_area,

                    ]
                )
            ]
        ))

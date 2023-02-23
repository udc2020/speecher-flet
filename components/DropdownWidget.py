from flet import *


class DropDownWidget (UserControl):

    _hint_text: str
    _list_drop: list
    _on_change: any
    _drop: Dropdown
    _value: str

    def __init__(self, list_drop, hint_text, on_change):

        super().__init__()

        self._list_drop = list_drop
        self._hint_text = hint_text
        self._on_change = on_change

    def get_value(self):
        self._value = self._drop.value
        return self._value

    def build(self):
        self._drop = Dropdown(
            hint_text=self._hint_text,
            bgcolor="white",
            text_style=TextStyle(
                color=colors.BLACK,
                size=18
            ),
            options=list(
                map(
                    lambda l: dropdown.Option(l),
                    self._list_drop
                )),
            on_change=self._on_change
        )
        return self._drop

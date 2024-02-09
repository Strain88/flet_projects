import flet as ft  # type: ignore


money_button_style: dict = {
    "border_radius": 5,
    "border": ft.border.all(1.25, "white54"),
    "padding": ft.padding.only(left=25, right=25, top=10, bottom=10),
    "animate": ft.Animation(350, "ease"),
}


class MoneyButton(ft.Container):
    def __init__(self, name: str, transaction_row: object, info: str):
        super().__init__(**money_button_style,
                         on_click=self.selected)
        self.info = info
        self.data = self.info
        self.transaction_row = transaction_row
        self.content = ft.Text(name, color="white")

    def selected(self, e: ft.TapEvent):
        for item in self.transaction_row.controls:
            item.border = (
                ft.border.all(1.25, "teal")
                if item == e.control
                else ft.border.all(1.25, "white54")
            )
            item.data = self.info if item == e.control else None
            item.update()

import flet as ft  # type: ignore
import utils


class InputView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__(
            route="/input",
            horizontal_alignment="center",
            padding=0,
            bgcolor="#131721",
            )

        self.page = page

        self.text = ft.TextField(
            color="white",
            text_align="center",
            border_color="white70",
            cursor_color="white",
            height=50,
            focused_border_color="teal",
            width=320,
        )

        self.transaction_row = ft.Row(alignment="center")
        self.transaction_row.controls = [
            utils.MoneyButton("Money In", self.transaction_row, "in"),
            utils.MoneyButton("Money Out", self.transaction_row, "out"),
        ]

        self.records = ft.Text(
            spans=[
                ft.TextSpan(
                    "Leger",
                    style=ft.TextStyle(color="white"),
                    on_click=lambda _: self.page.go("/output"))
            ]
        )

        self.controls = [
            ft.Container(
                height=50,
                bgcolor="#1d212b",
                padding=ft.padding.only(left=20, right=20),
                content=ft.Row(
                    alignment="spaceBetween",
                    controls=[
                        ft.Text("My Ledger", color="white"),
                        self.records
                    ]
                ),
            ),
            ft.Divider(height=30, color="transparent"),
            ft.Column(
                spacing=20,
                horizontal_alignment="center",
                controls=[
                    ft.Text("Transaction Type", weight="w700", color="white"),
                    self.transaction_row,

                ],
            ),
            ft.Divider(height=30, color="transparent"),
            ft.Column(
                horizontal_alignment="center",
                spacing=20,
                controls=[
                    ft.Text("Amount", weight="w700", color="white"),
                    ft.Row(
                        alignment="center",
                        controls=[ft.Container(
                            border_radius=5,
                            border=ft.border.all(1.25, "white24"),
                            content=self.text,
                            ),
                        ],
                    ),
                ],
            ),
            ft.Column(
                alignment="center",
                expand=True,
                controls=[
                    ft.Container(
                        bgcolor="#1d212b",
                        height=50,
                        on_click=self.submit,
                        content=ft.Row(
                            alignment="center",
                            controls=[ft.Text("Submit", color="white")],
                        ),
                    ),
                ],
            ),
        ]

    def submit(self, e: ft.TapEvent):
        for item in self.transaction_row.controls:
            if item.data == "in":
                self.add_value()
            elif item.data == "out":
                self.subtract_value()

    def add_value(self):
        if self.text.value:
            utils.Controller.add_to_ledger(self.text.value)
            self.text.value = None

        self.text.update()

    def subtract_value(self):
        if self.text.value:
            utils.Controller.subtract_from_ledger(self.text.value)
            self.text.value = None

        self.text.update()


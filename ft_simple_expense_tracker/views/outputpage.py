import flet as ft  # type: ignore
import utils


class OutputView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__(
            route="/output",
            horizontal_alignment="center",
            padding=0,
            bgcolor="#131721",
            )

        self.page = page

        self.ledger: dict = utils.Controller.get_leger()
        self.input_page = ft.Text(
            size=16,
            spans=[
                ft.TextSpan(
                    "Back",
                    style=ft.TextStyle(color="white"),
                    on_click=lambda _: self.page.go("/input")),
            ],
        )

        self.balance = ft.Text(
            f"Total balance: {sum(self.ledger.values())}",
            color="white",
            size=11,
        )

        self.number = ft.Text(
            f"No. of records: {len(self.ledger)}",
            color="white",
            size=11,
        )

        self.controls = [
            ft.Row(
                controls=[
                    ft.Text("Recors", size=16),
                    self.input_page,
                ],
                alignment="spaceBetween",
            ),
            ft.Row(
                controls=[self.number, self.balance],
                alignment="spaceBetween"),
            *[
                ft.Column(
                    controls=[
                        ft.Row(
                            controls=[
                                ft.Text(
                                    key.strftime("%b %d, %Y"),
                                    color="white",
                                ),
                                ft.Text(
                                    value,
                                    color="white",
                                ),
                            ],
                            alignment="spaceBetween",
                        ),
                        ft.Divider(height=2, color="white10"),
                    ],
                )
                for key, value in self.ledger.items()
            ]
        ]

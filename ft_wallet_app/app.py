import flet as ft  # type: ignore


class App(ft.UserControl):
    """
    Class to geenrate cards
    """
    COLORPICK = 0

    ColorList: dict = {
        "start": ["#13547a", "#f43b47", "#30cfd0", "#243949"],
        "end": ["#80d0c7", "#453a94", "#330867", "#517fa4"],
    }

    def build(self) -> ft.Column:
        self.InsertButton: ft.Container = ft.Container(
            content=ft.IconButton(
                on_click=lambda e: self.OpenEntryForm(),
                icon="add",
                icon_size=15,
            ),
            alignment=ft.alignment.center_right,
            padding=ft.padding.only(0, 0, 10, 0),
        )

        self.Title = ft.Text(
            value="Wallite",
            size=22
        )

        self.CardWallet = ft.Row()

        self.CardName = ft.TextField(
            label="Card Name",
            border="underline",
            text_size=12,
        )

        self.CardNumber = ft.TextField(
            label="Card Number",
            border="underline",
            text_size=12,
        )

        self.EntryForm = ft.AlertDialog(
            title=ft.Text(
                "Enter Your Bank Name\nCard Name",
                text_align="center",
                size=12,
            ),
            content=ft.Column(
                controls=[
                    self.CardName,
                    self.CardNumber,
                ],
                spacing=20,
                height=180,
            ),
            actions=[
                ft.TextButton(
                    text="Insert",
                    on_click=lambda e: self.CheckEntryForm(),
                ),
                ft.TextButton(
                    text="Cancel",
                    on_click=lambda e: self.CancelEntryForm(),
                ),
            ],
            actions_alignment="center",
            on_dismiss=lambda e: self.CancelEntryForm(),
        )

        _obj = ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        self.EntryForm,
                        ft.Container(
                            width=160,
                            content=self.Title,
                            padding=ft.padding.all(10),
                        ),
                        ft.Container(
                            width=160,
                            content=self.InsertButton,
                            alignment=ft.alignment.center_right,
                            padding=ft.padding.all(10),
                        ),
                    ],
                    alignment="spaceAround",
                ),
                ft.Row(
                    wrap=False,
                    scroll="auto",
                    controls=[
                        ft.Container(
                            padding=ft.padding.only(10, 0, 10, 0),
                            content=self.CardWallet,
                        ),
                    ],
                ),
            ]
        )
        return _obj

    def CheckEntryForm(self):
        if len(self.CardNumber.value) == 0:
            self.CardNumber.error_text = "Please enter your number!"
            self.update()
        else:
            self.CardNumber.error_text = None
            self.update()

        if len(self.CardName.value) == 0:
            self.CardName.error_text = "Please enter your cvv!"
            self.update()
        else:
            self.CardName.error_text = None
            self.update()

        if len(self.CardNumber.value) and (len(self.CardName.value)) != 0:
            self.CardMaker()

    def OpenEntryForm(self):
        self.dialog = self.EntryForm
        self.EntryForm.open = True
        self.update()

    def CancelEntryForm(self):
        self.CardName.value, self.CardNumber.value = None, None
        self.CardNumber.error_text, self.CardName.error_text = None, None
        self.EntryForm.open = False
        self.update()

    def CardMaker(self):

        self.img = ft.Image()
        if self.CardNumber.value[0] == "4":  # visa
            self.img = ft.Image(
                src="./assets/icons8-visa-200(-xxxhdpi).png",
                width=80,
                height=80,
                fit="contain",
            )
        elif self.CardNumber.value[0] == "5":  # mastercard
            self.img = ft.Image(
                src="./assets/icons8-mastercard-logo-100.png",
                width=80,
                height=80,
                fit="contain",
            )
        elif self.CardNumber.value[0] == "3":
            ...
        else:
            ...

        self.card = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Container(
                        content=ft.Text(
                            self.CardName.value,
                            size=20,
                        ),
                        alignment=ft.alignment.top_left,
                    ),
                    ft.Row(
                        controls=[
                            ft.TextButton(
                                content=ft.Container(
                                    alignment=ft.alignment.bottom_left,
                                    content=ft.Column(
                                        [
                                            ft.Text(
                                                value=f"**** **** **** {self.CardNumber.value[-4:]}",
                                                size=14,
                                                color=ft.colors.WHITE,
                                                height=20,
                                            ),
                                        ],
                                    ),
                                    on_click=None,
                                ),
                            ),
                            ft.Container(
                                content=(self.img),
                                alignment=ft.alignment.bottom_right,
                            ),
                        ],
                        alignment="spaceBetween",
                    ),
                ],
                alignment="spaceBetween",
            ),
            border_radius=ft.border_radius.all(20),
            width=280,
            height=180,
            padding=ft.padding.all(10),
            gradient=ft.LinearGradient(
                begin=ft.alignment.bottom_left,
                end=ft.alignment.top_right,
                colors=[
                    App.ColorList["start"][self.COLORPICK],
                    App.ColorList["end"][self.COLORPICK],
                ],
            ),
        )

        self.COLORPICK = (self.COLORPICK + 1) % 4

        self.CardWallet.controls.append(self.card)
        self.CancelEntryForm()
        self.update()

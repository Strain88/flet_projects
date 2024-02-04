import flet as ft  # type: ignore


class Landing(ft.View):
    def __init__(self, page: ft.Page) -> None:
        super().__init__(
            route="/",
            horizontal_alignment="center",
            vertical_alignment="center",
        )

        self.page = page

        self.cart_logo = ft.Icon(
            name="shopping_cart_outlined",
            size=64,
        )
        self.title = ft.Text(
            "Simple Store",
            size=28,
            weight="bold",
            )
        self.subtitle = ft.Text(
            "Made with Flet",
            size=11,
            weight="bold",
            )
        self.product_page_btn = ft.IconButton(
            icon="arrow_forward",
            width=54,
            height=54,
            style=ft.ButtonStyle(
                bgcolor={"": "#202020"},
                shape={"": ft.RoundedRectangleBorder(radius=8)},
                side={"": ft.BorderSide(2, "white54")},
            ),
            on_click=lambda e: self.page.go("/products")
        )

        self.controls = [
            self.cart_logo,
            ft.Divider(height=25, color="transparent"),
            self.title,
            self.subtitle,
            ft.Divider(height=10, color="transparent"),
            self.product_page_btn,
        ]

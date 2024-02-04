import flet as ft  # typo: ignore
from views.landing import Landing
from views.product import Product
from views.cart import Cart


def main(page: ft. Page) -> None:
    page.title = "Shop"
    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    # page.window_width = 320
    # page.window_height = 640

    def router(route: str):
        page.views.clear()

        if page.route == "/":
            landing = Landing(page)
            page.views.append(landing)

        if page.route == "/products":
            products = Product(page)
            page.views.append(products)

        if page.route == "/cart":
            cart = Cart(page)
            page.views.append(cart)

        page.update()

    page.on_route_change = router
    page.go("/")


ft.app(target=main, assets_dir="assets")

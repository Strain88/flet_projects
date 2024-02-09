import flet as ft  # type: ignore
from views import InputView, OutputView


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT

    def router(route: str):
        page.views.clear()

        if page.route == "/input":
            input_view = InputView(page)
            page.views.append(input_view)
        elif page.route == "/output":
            output_view = OutputView(page)
            page.views.append(output_view)
        page.update()

    page.on_route_change = router
    page.go("/input")


ft.app(target=main)

from datetime import datetime


class Controller():
    ledger: dict = {}

    @staticmethod
    def get_leger() -> dict:
        return Controller.ledger

    @staticmethod
    def add_to_ledger(value: str) -> None:
        Controller.ledger[datetime.now()] = int(value)

    @staticmethod
    def subtract_from_ledger(value: str) -> None:
        Controller.ledger[datetime.now()] = int(value) * -1

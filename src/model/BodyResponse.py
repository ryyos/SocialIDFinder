class BodyResponse:
    def __init__(self, status: int, message: str, data: dict) -> None:
        self.status: int = status
        self.message: str = message
        self.data: dict = data
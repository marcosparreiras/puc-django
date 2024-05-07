class UnauthorizedException(Exception):
    def __init__(self) -> None:
        super().__init__(f"Unauthorized")

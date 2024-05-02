class StudentNotFoundException(Exception):
    def __init__(self, student: str) -> None:
        super().__init__(f"Student ({student}) not found")

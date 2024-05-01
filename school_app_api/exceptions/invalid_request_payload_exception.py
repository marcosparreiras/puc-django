from typing import Dict


class InvalidRequestPayloadException(Exception):
    def __init__(self, errors: Dict[str, any]) -> None:
        super().__init__("Invalid request payload")
        self._errors = errors

    def getErrors(self) -> Dict[str, any]:
        return self._errors

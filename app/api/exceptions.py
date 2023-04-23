from fastapi import status


class CRUDError(Exception):
    def __init__(self, status_code: int, message: str):
        super().__init__(message)
        self.status_code = status_code
        self.message = message


class NotFound(CRUDError):
    def __init__(self, message: str = "Not found"):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND, message=message
        )


class IncorrectAuthRequest(CRUDError):
    def __init__(self, message: str = "Incorrect email or password"):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST, message=message
        )


class QuestAlreadyCompleted(CRUDError):
    def __init__(
        self, message: str = "Quest has been already completed by this user"
    ):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST, message=message
        )


class TrophyHasHash(CRUDError):
    def __init__(self, message: str = "This trophy already has hash"):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST, message=message
        )

from fastapi import HTTPException


class HTTPExceptionBase(HTTPException):
    def __init__(self, status_code: int, detail: str):
        self.status_code = status_code
        self.detail = detail


NotFound = HTTPExceptionBase(404, "Не найдено")

from fastapi import HTTPException


class HTTPExceptionBase(Exception):
    def __init__(self, status_code: int, detail: str):
        self.status_code = status_code
        self.detail = detail

    def get_http_exception(self):
        return HTTPException(self.status_code, self.detail)


NotFound = HTTPExceptionBase(404, "Не найдено")
Forbidden = HTTPExceptionBase(403, "Доступ к ресурсу запрещён")
CategoryNotExist = HTTPExceptionBase(404, "Категории с таким ID не существует")
BalanceNotExist = HTTPExceptionBase(404, "Баланса с таким ID не существует")

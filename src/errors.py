from types import TracebackType
from typing import Optional


class ComplexExtractException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    def with_traceback(self, tb: Optional[TracebackType]) -> BaseException:
        return super().with_traceback(tb)

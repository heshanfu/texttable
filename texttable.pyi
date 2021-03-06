from typing import *

class Texttable:

    BORDER: int
    HEADER: int
    HLINES: int
    VLINES: int

    def __init__(self, max_width: int = ...) -> None: ...

    def reset(self) -> None: ...

    def set_chars(self, array: List[str]) -> None: ...

    def set_deco(self, deco: int) -> None: ...

    def set_header_align(self, array: List[str]) -> None: ...

    def set_cols_align(self, array: List[str]) -> None: ...

    def set_cols_valign(self, array: List[str]) -> None: ...

    def set_cols_dtype(self, array: List[Union[str, Callable[[Any], str]]]) -> None: ...

    def set_cols_width(self, array: List[int]) -> None: ...

    def set_precision(self, width: int) -> None: ...

    def header(self, array: List[str]) -> None: ...

    def add_row(self, array: List[Union[Union[int, str], float]]) -> None: ...

    def add_rows(self, rows: List[object], header: bool = ...) -> None: ...

    def draw(self) -> str: ...

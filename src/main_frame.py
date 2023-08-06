import tkinter as tk
from tkinter import _Cursor, _Relief, _ScreenUnits, _TakeFocusValue, Misc
from tkinter.font import _FontDescription
from typing import Any
from typing_extensions import Literal


class MainFrame(tk.LabelFrame):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        
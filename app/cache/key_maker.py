import inspect
from typing import Callable


class KeyMaker():
    async def make(self, function: Callable, prefix: str) -> str:
        # path = f"{prefix}::{function.__name__}"
        path = f"{prefix}::{inspect.getmodule(function).__name__}.{function.__name__}"
        args = ""

        for arg in inspect.signature(function).parameters.values():
            args += arg.name

        if args:
            return f"{path}.{args}"

        return path

import contextlib
import inspect
from pathlib import Path
from types import FrameType
from typing import Callable, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")

key_stack = []

_auto_key_delimiter = "--"


def key_stack_is_empty():
    global key_stack
    return len(key_stack) == 0


def _key_stack_to_key(key_stack_: list[str]):
    return _auto_key_delimiter.join(key_stack_)


def get_key(key: str):
    global key_stack
    return _key_stack_to_key([*key_stack, key])


@contextlib.contextmanager
def auto_key_layer(key_layer: str):
    global key_stack
    try:
        key_stack.append(key_layer)
        yield _key_stack_to_key(key_stack)
    finally:
        key_stack.pop()


def auto_key(key_prefix: str = None):
    # gets line number of where auto_key is called
    caller_frame = inspect.currentframe().f_back
    _auto_key_internal(current_frame=caller_frame, key_prefix=key_prefix)


def _auto_key_internal(current_frame: FrameType = None, key_prefix: str = None):
    """creates a key based on a Frame, giving you a line number to reference"""
    global key_stack

    called_in_relative_filepath = Path(current_frame.f_code.co_filename).relative_to(
        Path.cwd()
    )
    called_at_line_no = current_frame.f_lineno
    if key_prefix is not None:
        key_layer = (
            f"<{key_prefix}> @ {called_in_relative_filepath}[{called_at_line_no}]"
        )
    else:
        key_layer = f"{called_in_relative_filepath}[{called_at_line_no}]"

    if len(key_stack) > 0:
        return get_key(key_layer)
    else:
        return key_layer


def enable_auto_keyed_widget(widget_fn: Callable[P, R]) -> Callable[P, R]:
    def _auto_keyed_widget(*args, **kwargs):
        # gets line number of where auto_keyed widget is called
        caller_frame = inspect.currentframe().f_back

        if len(args) < 2 and "key" not in kwargs.keys():
            kwargs["key"] = _auto_key_internal(
                current_frame=caller_frame, key_prefix=widget_fn.__name__
            )
        return widget_fn(*args, **kwargs)

    return _auto_keyed_widget

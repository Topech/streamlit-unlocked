import inspect
from pathlib import Path
from typing import Callable, ParamSpec, TypeVar

import streamlit as st

from src.auto_key import auto_key_layer

P = ParamSpec("P")
R = TypeVar("R")

# inputs -> go in


def smart_fragment(fn: Callable[P, R]) -> Callable[P, R | None]:
    def _decorated_fragment(*args, **kwargs):
        caller_frame = inspect.currentframe().f_back
        raw_used_in_file = caller_frame.f_code.co_filename
        used_in_file = Path(raw_used_in_file).relative_to(Path.cwd())
        used_at_line_no = caller_frame.f_lineno

        raw_declared_in_file = inspect.getmodule(fn).__file__
        declared_in_file = Path(raw_declared_in_file).relative_to(Path.cwd())
        declared_at_line_no = fn.__code__.co_firstlineno

        key_layer = f"<{declared_in_file}[{declared_at_line_no}]:{fn.__name__}> @ {used_in_file}[{used_at_line_no}]"

        with auto_key_layer(key_layer):
            # todo: persist key_layer within a fragment after first call (the external key stack isn't recreated - only code in fragment runs)
            # output = st.fragment(fn)(*args, **kwargs)
            output = fn(*args, **kwargs)

        if output is not None:
            st.session_state[fn.__name__] = output
            # todo: some way to better scope reruns?
            st.rerun(scope="app")

        return output

    return _decorated_fragment


# output -> None, only callbacks?

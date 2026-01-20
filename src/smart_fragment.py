import inspect
from typing import Callable, ParamSpec, TypeVar

import streamlit as st

from src.auto_key import auto_key_layer

P = ParamSpec("P")
R = TypeVar("R")

# inputs -> go in


def smart_fragment(fn: Callable[P, R]) -> Callable[P, R | None]:
    def _decorated_fragment(*args, **kwargs):
        caller_frame = inspect.currentframe().f_back
        used_in_file = caller_frame.f_code.co_filename
        used_at_line_no = caller_frame.f_lineno

        key_layer = f"<{fn.__name__}>{used_in_file}:{used_at_line_no}"

        with auto_key_layer(key_layer):
            output = st.fragment(fn)(*args, **kwargs)

        if output is not None:
            st.session_state[fn.__name__] = output
            # todo: some way to better scope reruns?
            st.rerun(scope="app")

        return output

    return _decorated_fragment


# output -> None, only callbacks?

import inspect
from pathlib import Path
from typing import Callable, ParamSpec, TypeVar

import streamlit as st

from src.auto_key import (
    auto_key_layer,
    get_key,
    key_stack_is_empty,
)

P = ParamSpec("P")
R = TypeVar("R")

# inputs -> go in


def smart_fragment(fn: Callable[P, R]) -> Callable[P, R | None]:
    def _create_fragment_closure(*args, **kwargs):
        caller_frame = inspect.currentframe().f_back
        raw_used_in_file = caller_frame.f_code.co_filename
        used_in_file = Path(raw_used_in_file).relative_to(Path.cwd())
        used_at_line_no = caller_frame.f_lineno

        raw_declared_in_file = inspect.getmodule(fn).__file__
        declared_in_file = Path(raw_declared_in_file).relative_to(Path.cwd())
        declared_at_line_no = fn.__code__.co_firstlineno

        key_layer = f"<{fn.__name__}: {declared_in_file}[{declared_at_line_no}]> @ {used_in_file}[{used_at_line_no}]"

        # NOTE: we get root key layer out of closure to 'persist' it for fragment reruns
        fragment_root_key_layer = get_key(key_layer)

        @st.fragment
        def _fragment_closure(*args, **kwargs):
            # differentiates if the fragment is running in isolation OR as part of whole app re-run
            if key_stack_is_empty():
                # TODO: # restore_key_stack_for_smart_fragment(fragment_root_key_layer)
                fragment_key_layer = fragment_root_key_layer
            else:
                fragment_key_layer = key_layer

            with auto_key_layer(fragment_key_layer) as generated_fragment_key:
                output = fn(*args, **kwargs)

            # this is odd, but the output is returned on re-run, so this is actually getting the output from before the
            # triggered rerun
            previous_output = st.session_state.get(generated_fragment_key, None)

            # save the output for next re-run
            st.session_state[generated_fragment_key] = output

            if output is not None:
                # todo: some way to better scope reruns?
                st.rerun(scope="app")
            return previous_output

        return _fragment_closure(*args, **kwargs)

    return _create_fragment_closure


# output -> None, only callbacks?

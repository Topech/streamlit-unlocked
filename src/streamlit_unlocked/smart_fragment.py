import inspect
from pathlib import Path
from typing import Callable, Literal, ParamSpec, TypeAlias, TypeVar, Union

import streamlit as st

from src.streamlit_unlocked import auto_key

P = ParamSpec("P")
R = TypeVar("R")

# inputs -> go in


SmartFragmentReturnStrategies: TypeAlias = Union[
    Literal["rerun_not_on_none"], Literal["rerun_on_change"], Literal["no_rerun"]
]


def smart_fragment(
    fn: Callable[P, R] = None,
    *,
    on_return_strategy: SmartFragmentReturnStrategies = "rerun_on_not_none",
) -> Callable[P, R]:
    def _closed_parameters_decorator(fn):
        """this layer justs lets us optionally provide parameters"""

        def _frame_intercepting_wrapper(*args, **kwargs):
            caller_frame = inspect.currentframe().f_back
            raw_used_in_file = caller_frame.f_code.co_filename
            used_in_file = Path(raw_used_in_file).relative_to(Path.cwd())
            used_at_line_no = caller_frame.f_lineno

            raw_declared_in_file = inspect.getmodule(fn).__file__
            declared_in_file = Path(raw_declared_in_file).relative_to(Path.cwd())
            declared_at_line_no = fn.__code__.co_firstlineno

            key_layer = f"<{fn.__name__}: {declared_in_file}[{declared_at_line_no}]> @ {used_in_file}[{used_at_line_no}]"

            # NOTE: we get root key layer out of inner_fragment to 'persist' it for fragment reruns
            fragment_root_key_layer = auto_key.get_key(key_layer)

            @st.fragment
            def _wrapped_fragment(*args, **kwargs):
                # differentiates if the fragment is running in isolation OR as part of whole app re-run
                if auto_key.key_stack_is_empty():
                    fragment_key_layer = fragment_root_key_layer
                else:
                    fragment_key_layer = key_layer

                with auto_key.auto_key_layer(
                    fragment_key_layer
                ) as generated_fragment_key:
                    output = fn(*args, **kwargs)

                fragment_result_key = f"RETURN: {generated_fragment_key}"

                _is_first_time_calling_fragment = (
                    fragment_result_key not in st.session_state
                )

                if not _is_first_time_calling_fragment:
                    previous_output = st.session_state.get(fragment_result_key, None)

                # save the output for next re-run
                st.session_state[fragment_result_key] = output

                # reruns should only occur after the first fragment run (otherwise you're in a loop anyways)
                if not _is_first_time_calling_fragment:
                    _do_rerun_strategy(
                        previous_output, output, on_return_strategy=on_return_strategy
                    )

                # this is odd, but the output is returned on re-run, so this is actually getting the output from before the
                # triggered rerun
                return_value = (
                    output if _is_first_time_calling_fragment else previous_output
                )
                return return_value

            return _wrapped_fragment(*args, **kwargs)

        return _frame_intercepting_wrapper

    if fn is None:
        return _closed_parameters_decorator
    else:
        # NOTE: all other parameters will be their defaults
        return _closed_parameters_decorator(fn)


def _do_rerun_strategy(
    old_value: R, output: R, *, on_return_strategy: SmartFragmentReturnStrategies
):
    if on_return_strategy == "rerun_not_on_none" and output is not None:
        st.rerun(scope="app")

    if on_return_strategy == "rerun_on_change" and output != old_value:
        st.rerun(scope="app")

import streamlit as st

from src.smart_fragment import smart_fragment
from src.widgets import button


@smart_fragment
def my_smart_frag():
    hello_btn = button.button("hello")

    if hello_btn:
        button.button("there")
        button.pills("pills", options=["a", "b", "c"])


my_smart_frag()
my_smart_frag()

st.session_state

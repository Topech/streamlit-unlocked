import streamlit as st

from src.auto_key import auto_key, auto_key_layer
from src.widgets import button


def reusable_1():
    with auto_key_layer("autokeycontext1"):
        button.button("label1")
        ...
        with auto_key_layer("autokeycontext2"):
            button.button("label2")

    with auto_key_layer("autokeycontext3"):
        st.pills("wow", options="abc", key=auto_key())


reusable_1()
reusable_1()


def auto_keyed_widget_test():
    with auto_key_layer("x"):
        col1, col2 = st.columns(2)
        with col1:
            button.button("a")
        with col2:
            button.button("b")


auto_keyed_widget_test()
auto_keyed_widget_test()

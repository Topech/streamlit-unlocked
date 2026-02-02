import streamlit as st

import streamlit_unlocked as stu
from streamlit_unlocked.auto_key import auto_key_layer


def reusable_1():
    with auto_key_layer("autokeycontext1"):
        stu.button("label1")
        ...
        with auto_key_layer("autokeycontext2"):
            stu.button("label2")

    with auto_key_layer("autokeycontext3"):
        stu.pills("wow", options="abc")


reusable_1()


def auto_keyed_widget_test():
    with auto_key_layer("x"):
        col1, col2 = st.columns(2)
        with col1:
            stu.button("a")
        with col2:
            stu.button("a")


auto_keyed_widget_test()

import streamlit as st

import streamlit_unlocked as stu


@stu.smart_fragment
def my_smart_frag():
    hello_btn = stu.button("hello")

    if hello_btn:
        stu.button("there")
        stu.pills("pills", options=["a", "b", "c"])


my_smart_frag()
my_smart_frag()

st.session_state

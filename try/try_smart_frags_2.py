import datetime as dt

import streamlit as st

import src as stu
from src import smart_fragment


@smart_fragment
def x():
    """testing"""
    st.write("a")
    "# hello"
    "test"


@smart_fragment(on_return_strategy="no_rerun")
def y():
    val = stu.toggle("a")
    stu.toggle("b")

    return val


x()
x()
res = y()
save_btn = st.button("save")

st.write(dt.datetime.now())

st.session_state

if save_btn:
    st.write(res)

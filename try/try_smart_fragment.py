import streamlit as st

from src.auto_key import auto_key
from src.smart_fragment import smart_fragment


@smart_fragment
def frag_1():
    st.button("1", key=auto_key())


@smart_fragment
def frag_2():
    frag_1()
    "--"
    st.button("1", key=auto_key())
    st.button("2", key=auto_key())


@smart_fragment
def frag_3():
    frag_2()
    "----"
    frag_2()


frag_3()

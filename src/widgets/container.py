import streamlit as st

from src.auto_key import enable_auto_keyed_widget

container = enable_auto_keyed_widget(st.container)

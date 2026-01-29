import streamlit as st

from src.auto_key import enable_auto_keyed_widget

data_editor = enable_auto_keyed_widget(st.data_editor)

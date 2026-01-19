import streamlit as st

from src.auto_key import enable_auto_keyed_widget

button = enable_auto_keyed_widget(st.button)
link_button = st.link_button  # note: doesn't have key parameter
download_button = enable_auto_keyed_widget(st.download_button)
pills = enable_auto_keyed_widget(st.pills)

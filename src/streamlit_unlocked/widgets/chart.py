import streamlit as st

from streamlit_unlocked.auto_key import enable_auto_keyed_widget

plotly_chart = enable_auto_keyed_widget(st.plotly_chart)
vega_lite_chart = enable_auto_keyed_widget(st.vega_lite_chart)

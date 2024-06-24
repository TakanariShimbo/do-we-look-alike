import streamlit as st

from model import LOGO_SVG


class AppConfig:
    @staticmethod
    def set_app_config() -> None:
        st.set_page_config(
            page_title="Do We Look Alike?",
            page_icon=LOGO_SVG,
            layout="centered",
        )

        # Hide Streamlit Style
        hide_streamlit_style = """
            <style>
            [data-testid="stToolbar"] {visibility: hidden !important;}
            footer {visibility: hidden !important;}
            </style>
        """
        st.markdown(hide_streamlit_style, unsafe_allow_html=True)
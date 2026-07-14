from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components


APP_DIR = Path(__file__).parent
INDEX_HTML = APP_DIR / "index.html"


st.set_page_config(
    page_title="Van Dispatch Board",
    page_icon="🚐",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
      .block-container { padding: 0; max-width: 100%; }
      header[data-testid="stHeader"] { display: none; }
      footer { display: none; }
      iframe { display: block; }
    </style>
    """,
    unsafe_allow_html=True,
)

html = INDEX_HTML.read_text(encoding="utf-8")

# Render the original single-file dispatch board inside Streamlit.
# The board still owns its UI/state; Streamlit supplies the hosting shell.
components.html(html, height=1800, scrolling=True)

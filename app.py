from pathlib import Path
import base64
import json

import streamlit as st
import streamlit.components.v1 as components


APP_DIR = Path(__file__).parent
INDEX_HTML = APP_DIR / "index.html"
UPLOAD_MARKER = "<script>\n\"use strict\";"


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
      .upload-card {
        background: #181c26;
        border: 1px solid #2b3242;
        border-left: 3px solid #ffb627;
        border-radius: 10px;
        color: #e7ecf3;
        font-family: ui-monospace, Menlo, Consolas, monospace;
        margin: 0 0 10px;
        padding: 12px 14px;
      }
      .upload-card b { color: #ffb627; }
      .upload-card small { color: #8b95a7; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="upload-card">
      <b>Upload your own job PDF</b><br>
      <small>Pick a job-book PDF or .txt export here, then review the parsed preview inside the board and click Apply.</small>
    </div>
    """,
    unsafe_allow_html=True,
)

upload = st.file_uploader(
    "Job package",
    type=["pdf", "txt"],
    label_visibility="collapsed",
    help="The file is parsed in your browser by the dispatch board before you apply it.",
)

html = INDEX_HTML.read_text(encoding="utf-8")

if upload:
    payload = {
        "name": upload.name,
        "type": upload.type or "application/octet-stream",
        "data": base64.b64encode(upload.getvalue()).decode("ascii"),
    }
    payload_json = json.dumps(payload).replace("</", "<\\/")
    inject = f"<script>window.STREAMLIT_JOB_UPLOAD={payload_json};</script>\n"
    html = html.replace(UPLOAD_MARKER, inject + UPLOAD_MARKER, 1)
    st.success("Upload received. Review the board preview below, then click Apply.")

# Render the original single-file dispatch board inside Streamlit.
# The board still owns its UI/state; Streamlit supplies the hosting shell.
components.html(html, height=1800, scrolling=True)

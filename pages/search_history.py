import streamlit as st
import pandas as pd
from pathlib import Path

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Search History",
    page_icon="🕒",
    layout="wide"
)

# -----------------------------
# Load CSS
# -----------------------------
css_path = Path(__file__).parent.parent / "assets" / "style.css"

if css_path.exists():
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# -----------------------------
# Hero Section
# -----------------------------
st.markdown("""
<div class="hero">
    <h1>🕒 Search History</h1>
    <h3>Previously Searched Medicines</h3>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# Back Button
# -----------------------------
if st.button("⬅ Back to Home"):
    st.switch_page("pages/home.py")

st.markdown("---")

# -----------------------------
# Load Search History
# -----------------------------
try:
    history = pd.read_csv("data/search_history.csv")

    if history.empty:
        st.info("No search history available.")
    else:
        st.subheader("📋 Search History")
        st.dataframe(history, use_container_width=True)

except FileNotFoundError:
    st.error("search_history.csv not found inside the data folder.")
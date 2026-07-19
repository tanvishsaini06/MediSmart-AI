import streamlit as st

def show_disease(disease):

    st.markdown("""
    <h2 style='color:#FBBF24;'>🩺 Disease Information</h2>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div style="
    background:#111827;
    color:white;
    padding:20px;
    border-radius:15px;
    border-left:6px solid #F59E0B;
    margin-bottom:15px;
    ">

    <h3>🦠 {disease['Disease']}</h3>

    <p><b>⚠ Symptoms</b></p>

    <p>{disease['Symptoms']}</p>

    <hr>

    <p><b>💊 Recommended Medicine</b></p>

    <p>{disease['Recommended_Medicine']}</p>

    </div>
    """, unsafe_allow_html=True)
import streamlit as st

def show_medicine(result):

    st.markdown("""
    <h2 style='color:#60A5FA;'>💊 Medicine Information</h2>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"""
        <div style="
        background:#111827;
        color:white;
        padding:20px;
        border-radius:15px;
        border-left:6px solid #3B82F6;
        margin-bottom:15px;
        ">
        <h3>💊 {result['Medicine']}</h3>
        <p><b>🩺 Disease:</b> {result['Disease']}</p>
        <p><b>💉 Dosage:</b> {result['Dosage']}</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div style="
        background:#111827;
        color:white;
        padding:20px;
        border-radius:15px;
        border-left:6px solid #10B981;
        margin-bottom:15px;
        ">
        <p><b>📂 Category:</b> {result['Category']}</p>
        <p><b>💰 Price:</b> ₹{result['Price']}</p>
        <p><b>🔄 Alternative:</b> {result['Alternative']}</p>
        </div>
        """, unsafe_allow_html=True)
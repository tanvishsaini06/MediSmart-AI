import streamlit as st

st.set_page_config(page_title="MediSmart AI", page_icon="💊", layout="wide")

# ================= NAVBAR =================
st.markdown("""
<style>
.block-container{
    padding-top:0rem;
    padding-left:2rem;
    padding-right:2rem;
}

.navbar{
    background:#2563EB;
    padding:18px 25px;
    border-radius:14px;
    display:flex;
    justify-content:space-between;
    align-items:center;
    margin-bottom:35px;
    box-shadow:0 6px 25px rgba(0,0,0,.25);
}

.logo{
    font-size:30px;
    font-weight:bold;
    color:white;
}

.menu{
    font-size:26px;
    color:white;
}

.hero{
    text-align:center;
    padding:40px 20px;
    background:linear-gradient(135deg,#0F172A,#1E293B,#2563EB);
    border-radius:22px;
    margin-bottom:35px;
    box-shadow:0 10px 35px rgba(0,0,0,.35);
}

.hero h1{
    font-size:64px;
    color:white;
    margin-bottom:10px;
}

.hero h3{
    color:#E2E8F0;
    font-size:28px;
    margin-bottom:15px;
}

.hero p{
    color:#CBD5E1;
    font-size:20px;
    max-width:850px;
    margin:auto;
}

.footer{
    text-align:center;
    color:#94A3B8;
    padding:25px;
    margin-top:40px;
    border-top:1px solid #334155;
}
</style>
""", unsafe_allow_html=True)


# Hero Section
st.markdown("<div style='height:35px;'></div>", unsafe_allow_html=True)
st.markdown("""
<div class="hero">
    <h1>💊 MediSmart AI</h1>
    <h3>AI-Powered Smart Medicine Finder</h3>
    <p>
    Search medicines, get AI recommendations, view disease information,
    and find nearby pharmacies with live map directions.
    </p>
</div>
""", unsafe_allow_html=True)
 
 
st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
"""
<div style="text-align:center;">
<h3 style="color:#6EA8FE;">
🚀 Explore MediSmart AI
</h3>

<p style="font-size:18px;">
Use the feature cards below to access every module of the application.
</p>
</div>
""",
unsafe_allow_html=True
)

# ================= FEATURES =================
st.markdown("## 🚀 Quick Access")

col1, col2, col3 = st.columns([1,1,1],gap="large")

with col1:
    st.markdown("### 🔍 Medicine Search")
    st.write("Search medicines, alternatives and dosage.")
    if st.button("Open Medicine Search", use_container_width=True):
        st.switch_page("pages/Medicine_search.py")

with col2:
    st.markdown("### 📊 Dashboard")
    st.write("View analytics and search statistics.")
    if st.button("Open Dashboard", use_container_width=True):
        st.switch_page("pages/Dashboard.py")

with col3:
    st.markdown("### 🕒 Search History")
    st.write("Review previously searched medicines.")
    if st.button("Open Search History", use_container_width=True):
        st.switch_page("pages/Dashboard.py")
st.markdown("---")

# ================= TECHNOLOGIES =================
st.subheader("🛠 Technologies Used")

tech1, tech2, tech3, tech4 = st.columns(4)

tech1.metric("Python", "✓")
tech2.metric("Streamlit", "✓")
tech3.metric("Pandas", "✓")
tech4.metric("AI / ML", "✓")


# ================= FOOTER =================
st.markdown("""
<div class="footer">
    <h4>💊 MediSmart AI</h4>
    <p>Developed by <b>Harshveer Singh</b></p>
    <p>B.Tech Artificial Intelligence & Machine Learning</p>
    <p>© 2026 All Rights Reserved</p>
</div>
""", unsafe_allow_html=True)
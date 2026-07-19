import streamlit as st
st.markdown("## 💊 Medicine Search")

if st.button("⬅ Back to Home"):
    st.switch_page("pages/home.py")

from pages import home
st.set_page_config(
    page_title="Medicine Search",
    page_icon="💊",
    layout="wide"
)   
import pandas as pd
import matplotlib.pyplot as plt
import math
from pathlib import Path
from rapidfuzz import process

from utils.history import save_search, load_history
from utils.map import show_map
from models.recommendation_model import recommend_medicine

from components.medicine_card import show_medicine
from components.disease_card import show_disease
from components.pharmacy_table import show_pharmacy


st.markdown("""
    <div class="hero">
            <h1>💊 MediSmart AI</h1>
            <h3>Search Medicines</h3>
    </div>        
""", unsafe_allow_html=True)

col1,col2=st.columns([1,5])
with col1:
    if st.button(" Back", use_container_width=True):
        st.switch_page("pages/home.py")


def load_css():
    css_path = Path(__file__).parent.parent / "assets" / "style.css"
    with open(css_path, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def calculate_distance(lat1, lon1, lat2, lon2):
    return math.sqrt((lat2 - lat1) ** 2 + (lon2 - lon1) ** 2)


load_css()


# ----------------------------
# Load CSV Files
# ----------------------------

medicine_df = pd.read_csv("data/medicines.csv")
disease_df = pd.read_csv("data/diseases.csv")
pharmacy_df = pd.read_csv("data/pharmacies.csv")

medicine_list = medicine_df["Medicine"].tolist()

search = st.text_input("🔍 Search Medicine")

if search:

    with st.spinner("Searching..."):

     match = process.extractOne(search, medicine_list)

    if match and match[1] >= 70:

        result = medicine_df[
            medicine_df["Medicine"] == match[0]
        ].iloc[0]

        save_search(match[0])

        show_medicine(result)

        st.markdown("---")
        st.subheader("🤖 AI Medicine Recommendation")

        recommendations = recommend_medicine(result["Medicine"])

        if recommendations:
            for medicine in recommendations:
                st.markdown(f"""
                            <div style="
                            background:#111827;
                            color:white;
                            padding:15px;
                            border-radius:12px;
                            margin-bottom:10px;
                            border-left:6px solid #10B981;
                            ">
                            <h4>{medicine}</h4>
                            </div>
                            """, unsafe_allow_html=True)
                

        st.markdown("---")

        disease = disease_df[
            disease_df["Disease"] == result["Disease"]
        ]

        if not disease.empty:
            disease = disease.iloc[0]
            show_disease(disease)
            st.markdown("---")
        
        pharmacy = pharmacy_df[
            pharmacy_df["Medicine"].str.strip().str.lower()
            == result["Medicine"].strip().lower()
        ].copy()

        if not pharmacy.empty:

            # User Location (Village Khudda, Tanda)
            user_lat = 31.6698
            user_lon = 75.6392

            pharmacy["Distance (km)"] = pharmacy.apply(
                lambda row: round(
                    calculate_distance(
                        user_lat,
                        user_lon,
                        row["Latitude"],
                        row["Longitude"]
                    ),
                    2,
                ),
                axis=1,
            )

            pharmacy = pharmacy.sort_values("Distance (km)")

            show_pharmacy(pharmacy)
            st.markdown("---")
            st.subheader("🗺️ Pharmacy Locations")   
            show_map(pharmacy)  # Call show_map here with the filtered pharmacy dataframe

        else:
            st.warning("Medicine not available in any pharmacy.")

    else:
        st.error("❌ Medicine Not Found")

else:
    st.dataframe(
        medicine_df,
        use_container_width=True
    )
# =====================================
# Search Analytics
# =====================================

st.markdown("---")
st.subheader("🔍 Search Analytics")

history_df = pd.read_csv("data/search_history.csv")

if not history_df.empty:

    search_count = history_df["Medicine"].value_counts()

    analytics_df = search_count.reset_index()
    analytics_df.columns = ["Medicine", "Search Count"]

    st.dataframe(
        analytics_df,
        use_container_width=True
    )

    fig, ax = plt.subplots(figsize=(8, 4))

    ax.bar(
        analytics_df["Medicine"],
        analytics_df["Search Count"]
    )

    ax.set_title("Most Searched Medicines")
    ax.set_xlabel("Medicine")
    ax.set_ylabel("Search Count")

    plt.xticks(rotation=30)

    st.pyplot(fig)

else:
    st.info("No search history available.")

# =====================================
# Search History
# =====================================

st.markdown("---")
st.subheader("🕒 Search History")

history = load_history()

if not history.empty:
    st.dataframe(
        history,
        use_container_width=True
    )
else:
    st.info("No searches yet.")

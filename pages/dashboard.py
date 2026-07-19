import streamlit as st
st.markdown("## 💊 Medicine Search")

if st.button("⬅ Back to Home"):
    st.switch_page("pages/home.py")
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 MediSmart AI Dashboard")

# Load Data
medicine_df = pd.read_csv("data/medicines.csv")
disease_df = pd.read_csv("data/diseases.csv")
pharmacy_df = pd.read_csv("data/pharmacies.csv")

# ==========================
# Summary Cards
# ==========================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("💊 Total Medicines", len(medicine_df))

with col2:
    st.metric("🩺 Total Diseases", len(disease_df))

with col3:
    st.metric("🏥 Total Pharmacies", pharmacy_df["Pharmacy"].nunique())

st.markdown("---")

# ==========================
# Chart 1
# ==========================

st.subheader("💊 Medicines by Category")

category = medicine_df["Category"].value_counts()

fig, ax = plt.subplots(figsize=(6,4))
ax.bar(category.index, category.values)
ax.set_xlabel("Category")
ax.set_ylabel("Count")

st.pyplot(fig)

# ==========================
# Chart 2
# ==========================

st.subheader("🏥 Medicine Availability")

availability = pharmacy_df["Availability"].value_counts()

fig2, ax2 = plt.subplots(figsize=(5,5))
ax2.pie(
    availability.values,
    labels=availability.index,
    autopct="%1.1f%%"
)

st.pyplot(fig2)

# ==========================
# Top Rated Pharmacies
# ==========================

st.subheader("⭐ Top Rated Pharmacies")

top = pharmacy_df.sort_values(
    by="Rating",
    ascending=False
)

st.dataframe(
    top[
        [
            "Pharmacy",
            "Rating",
            "Address",
            "HomeDelivery"
        ]
    ].drop_duplicates(),
    use_container_width=True
)

st.markdown("---")
st.subheader("🔍 Search Analytics")

history_df = pd.read_csv("data/search_history.csv")

if not history_df.empty:

    search_count = history_df["Medicine"].value_counts()

    st.dataframe(
        search_count.reset_index().rename(
            columns={
                "index": "Medicine",
                "Medicine": "Search Count"
            }
        ),
        use_container_width=True
    )

    fig3, ax3 = plt.subplots(figsize=(7,4))

    ax3.bar(
        search_count.index,
        search_count.values
    )

    ax3.set_xlabel("Medicine")
    ax3.set_ylabel("Number of Searches")
    ax3.set_title("Most Searched Medicines")

    plt.xticks(rotation=30)

    st.pyplot(fig3)

else:
    st.info("No search history available.")
import folium
from streamlit_folium import st_folium
import streamlit as st
st.markdown("## 💊 Medicine Search")



def show_map(pharmacy_df):
    if pharmacy_df.empty:
        st.warning("No pharmacies found.")
        return
   

    if pharmacy_df.empty:
        st.warning("No pharmacies found.")
        return

    center_lat = pharmacy_df.iloc[0]["Latitude"]
    center_lon = pharmacy_df.iloc[0]["Longitude"]

    m = folium.Map(
        location=[center_lat, center_lon],
        zoom_start=13
    )

    for _, row in pharmacy_df.iterrows():

        popup = f"""
        <b>{row['Pharmacy']}</b><br>
        💰 Price: ₹{row['Price']}<br>
        ⭐ Rating: {row['Rating']}<br>
        📞 {row['Contact']}<br><br>

        <a href="https://www.google.com/maps/dir/?api=1&destination={row['Latitude']},{row['Longitude']}"
        target="_blank">
        📍 Get Directions
        </a>
        """

        folium.Marker(
            location=[row["Latitude"], row["Longitude"]],
            popup=popup,
            tooltip=row["Pharmacy"],
            icon=folium.Icon(color="green", icon="plus-sign")
        ).add_to(m)

    st_folium(
        m,
        width=None,
        height=500,
        use_container_width=True
    )
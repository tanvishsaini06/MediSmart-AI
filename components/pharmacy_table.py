import streamlit as st

def show_pharmacy(pharmacy_df):

    st.subheader("🏥 Pharmacy Availability")

    

    st.markdown("""
    <style>
    .stDataFrame{
        border:1px solid #d1d5db;
        border-radius:12px;
        overflow:hidden;
    }
    </style>
    """, unsafe_allow_html=True)

    st.dataframe(
        pharmacy_df,
        use_container_width=True,
        hide_index=True
    )

# Note: Do not call show_map here because `pharmacy_df` is provided
# as an argument to show_pharmacy. Call show_map from the caller
# where pharmacy_df is available, e.g. after preparing the dataframe.
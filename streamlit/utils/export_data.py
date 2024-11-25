import streamlit as st
from io import BytesIO

def export_data(data):
    st.title("Export Data")
    csv_data = data.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download Data as CSV",
        data=csv_data,
        file_name="vulnerabilities_data.csv",
        mime="text/csv",
    )

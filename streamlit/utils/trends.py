import streamlit as st
import pandas as pd


def render_trends(data):
    st.title("Time-Based Vulnerability Trends")
    date_col = 'vuln_list_0_HostAssetVuln_lastFound'
    if date_col in data.columns:
        st.subheader("Number of Vulnerabilities Over Time")
        data[date_col] = pd.to_datetime(data[date_col])
        trend_data = data.groupby(data[date_col].dt.to_period("M")).size().to_timestamp()
        st.line_chart(trend_data)

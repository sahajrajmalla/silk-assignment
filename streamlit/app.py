import streamlit as st
from utils.data_loader import load_data
from utils.map_visualization import render_map
from utils.anomaly_detection import detect_anomalies
from utils.export_data import export_data
from datetime import datetime

from utils.metrics import render_metrics
from utils.trends import render_trends

# App configuration
st.set_page_config(page_title="Vulnerability Dashboard", layout="wide")

# Load data
data = load_data()

# Sidebar navigation
st.sidebar.title("Navigation")
tabs = st.sidebar.radio("Go to", ["Overview", "Advanced Metrics", "Map Visualization", "Trend Analysis", "Anomaly Detection", "Export Data"])

st.sidebar.info("""
This dashboard was developed by **Sahaj Raj Malla** for an assignment at [Institution Name].
""")

# Tab handling
if tabs == "Overview":
    st.title("Overview of Vulnerability Data")
    st.dataframe(data)
    st.subheader("Basic Statistics")
    st.write(data.describe())
    st.subheader("Distribution of Vulnerabilities by Severity")
    if 'volume_list_0_HostAssetVolume_size' in data.columns:
        severity_counts = data['volume_list_0_HostAssetVolume_size'].value_counts()
        st.bar_chart(severity_counts)
    else:
        st.warning("Severity column not found in the dataset.")

elif tabs == "Advanced Metrics":
    render_metrics(data)
    
elif tabs == "Map Visualization":
    render_map(data)

elif tabs == "Trend Analysis":
    render_trends(data)

elif tabs == "Anomaly Detection":
    detect_anomalies(data)

elif tabs == "Export Data":
    export_data(data)

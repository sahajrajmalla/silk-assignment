import streamlit as st
from sklearn.ensemble import IsolationForest
import numpy as np

def detect_anomalies(data):
    st.title("Anomaly Detection in Vulnerabilities")
    numeric_columns = data.select_dtypes(include=[np.number]).columns
    if numeric_columns.empty:
        st.warning("No numeric columns available for anomaly detection.")
        return

    selected_col = st.selectbox("Select column for anomaly detection", numeric_columns)
    contamination = st.slider("Select contamination level", 0.01, 0.1, 0.05)
    model = IsolationForest(contamination=contamination, random_state=42)
    data['anomaly'] = model.fit_predict(data[[selected_col]])
    data['anomaly'] = data['anomaly'].map({1: 'Normal', -1: 'Anomaly'})
    st.write(data[['anomaly', selected_col]])
    st.bar_chart(data['anomaly'].value_counts())

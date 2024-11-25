import streamlit as st
from datetime import datetime
import pandas as pd
import numpy as np
def render_metrics(data):
    st.title("Advanced Metrics and Insights")

    if 'vuln_list_0_HostAssetVuln_lastFound' in data.columns:
        st.subheader("Vulnerability Aging Analysis")

        # Ensure datetime formats are consistent
        current_date = datetime.utcnow()
        data['vuln_list_0_HostAssetVuln_lastFound'] = data['vuln_list_0_HostAssetVuln_lastFound'].dt.tz_localize(None)

        # Calculate vulnerability age in days
        data['vulnerability_age_days'] = (current_date - data['vuln_list_0_HostAssetVuln_lastFound']).dt.days

        # Categorize vulnerabilities by age
        data['vulnerability_age_category'] = pd.cut(
            data['vulnerability_age_days'], 
            bins=[0, 30, 90, np.inf],
            labels=["New (0-30 days)", "Aging (31-90 days)", "Critical Aging (>90 days)"]
        )

        # Display aging category counts
        st.write("### Vulnerability Age Distribution")
        age_counts = data['vulnerability_age_category'].value_counts()
        st.bar_chart(age_counts)

        # Display aging details in a table
        st.write("### Detailed Aging Table")
        st.dataframe(data[['vuln_list_0_HostAssetVuln_lastFound', 'vulnerability_age_days', 'vulnerability_age_category']])

    else:
        st.warning("Required column 'vuln_list_0_HostAssetVuln_lastFound' is missing.")

    if 'vuln_list_0_HostAssetVuln_severity' in data.columns:
        st.subheader("Severity Analysis")
        severity_counts = data['vuln_list_0_HostAssetVuln_severity'].value_counts()
        st.write("### Vulnerability Severity Distribution")
        st.bar_chart(severity_counts)

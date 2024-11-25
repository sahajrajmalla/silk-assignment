import pandas as pd
import streamlit as st

def load_data():
    df = pd.read_csv("final_normal_df.csv", parse_dates=['vuln_list_0_HostAssetVuln_lastFound'])
    return df

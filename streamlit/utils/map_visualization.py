import streamlit as st
import pydeck as pdk
import pandas as pd

def render_map(data):
    st.title("Geographical Map of Vulnerabilities")
    
    # Ensure the required columns exist
    if 'agentInfo_locationGeoLatitude' in data.columns and 'agentInfo_locationGeoLongtitude' in data.columns:
        # Convert latitude and longitude to numeric, handling errors gracefully
        data['agentInfo_locationGeoLatitude'] = pd.to_numeric(data['agentInfo_locationGeoLatitude'], errors='coerce')
        data['agentInfo_locationGeoLongtitude'] = pd.to_numeric(data['agentInfo_locationGeoLongtitude'], errors='coerce')
        
        # Drop rows with missing or invalid lat/long values
        map_data = data.dropna(subset=['agentInfo_locationGeoLatitude', 'agentInfo_locationGeoLongtitude'])
        
        # Ensure lat/long values are within valid ranges
        map_data = map_data[
            (map_data['agentInfo_locationGeoLatitude'].between(-90, 90)) &
            (map_data['agentInfo_locationGeoLongtitude'].between(-180, 180))
        ]
        
        if not map_data.empty:
            # Add pydeck visualization
            st.pydeck_chart(pdk.Deck(
                map_style='mapbox://styles/mapbox/light-v9',
                initial_view_state=pdk.ViewState(
                    latitude=map_data['agentInfo_locationGeoLatitude'].mean(),
                    longitude=map_data['agentInfo_locationGeoLongtitude'].mean(),
                    zoom=6,
                    pitch=45,
                ),
                layers=[
                    pdk.Layer(
                        'ScatterplotLayer',
                        data=map_data,
                        get_position='[agentInfo_locationGeoLongtitude, agentInfo_locationGeoLatitude]',
                        get_color='[255, 0, 0, 160]',
                        get_radius=5000,
                        pickable=True,  # Allow click interactions
                    ),
                ],
                tooltip={
                    "html": """
                        <b>Latitude:</b> {agentInfo_locationGeoLatitude} <br>
                        <b>Longitude:</b> {agentInfo_locationGeoLongtitude} <br>
                        <b>Severity:</b> {agentInfo_status}
                    """,
                    "style": {"backgroundColor": "steelblue", "color": "white"}
                }
            ))
        else:
            st.warning("No valid latitude and longitude data available for plotting.")
    else:
        st.warning("Latitude and Longitude columns are missing in the dataset.")
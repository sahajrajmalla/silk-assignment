import pandas as pd
from api_client import fetch_data_from_api
from mongodb_operations import get_mongo_client, get_mongo_collection, create_unique_index
from data_processing import process_and_merge_data
from config import CROWDSTRIKE_URL, QUALYS_URL, CROWDSTRIKE_COLLECTION, QUALYS_COLLECTION

# Initialize MongoDB
client = get_mongo_client()
crowdstrike_collection = get_mongo_collection(client, CROWDSTRIKE_COLLECTION)
qualys_collection = get_mongo_collection(client, QUALYS_COLLECTION)

# Create unique indexes
create_unique_index(crowdstrike_collection, "hostname")
create_unique_index(qualys_collection, "name")

# Fetch and store Crowdstrike data
skip = 0
while True:
    data = fetch_data_from_api(CROWDSTRIKE_URL, skip)
    if not data:
        break
    for item in data:
        try:
            crowdstrike_collection.insert_one(item)
        except Exception:
            pass
    skip += len(data)

# Fetch and store Qualys data
skip = 0
while True:
    data = fetch_data_from_api(QUALYS_URL, skip)
    if not data:
        break
    for item in data:
        try:
            qualys_collection.insert_one(item)
        except Exception:
            pass
    skip += len(data)

# Load data from MongoDB
crowdstrike_data = list(crowdstrike_collection.find())
qualys_data = list(qualys_collection.find())

# Normalize and save data to MongoDB
final_df = process_and_merge_data(crowdstrike_data, qualys_data)
final_df.to_csv("streamlit/final_normal_df.csv", index=False)
print("Normalized data saved to 'final_normal_df.csv'")

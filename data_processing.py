import pandas as pd
from utils import normalize_to_single_table

def process_and_merge_data(crowdstrike_data, qualys_data):
    crowdstrike_df = normalize_to_single_table(crowdstrike_data)
    qualys_df = normalize_to_single_table(qualys_data)
    return pd.merge(qualys_df, crowdstrike_df, left_on='name', right_on='hostname', suffixes=('_qualys', '_crowdstrike'))

def save_to_mongodb(collection, data):
    for item in data:
        try:
            collection.insert_one(item)
            print(f"Inserted: {item['_id']}")
        except Exception as e:
            print(f"Error inserting data: {e}")

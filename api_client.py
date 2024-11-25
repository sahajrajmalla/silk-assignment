import requests
from config import HEADERS, BATCH_SIZE

def fetch_data_from_api(api_url, skip):
    """
    Fetch data from the given API URL with pagination.
    """
    params = {'skip': skip, 'limit': BATCH_SIZE}
    response = requests.post(api_url, params=params, headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    else:
        return []

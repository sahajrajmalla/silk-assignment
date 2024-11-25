# Configuration for MongoDB and API settings

# MongoDB Configuration
MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = "host_data"
CROWDSTRIKE_COLLECTION = "crowdstrike_hosts"
QUALYS_COLLECTION = "qualys_hosts"

# API Configuration
HEADERS = {
    'accept': 'application/json',
    'token': '__API_TOKEN__',
    'content-type': 'application/x-www-form-urlencoded',
}

# API Endpoints
CROWDSTRIKE_URL = 'https://api.recruiting.app.silk.security/api/crowdstrike/hosts/get'
QUALYS_URL = 'https://api.recruiting.app.silk.security/api/qualys/hosts/get'

# Pagination parameters
BATCH_SIZE = 1

import requests
import base64
import secrets

url = ''

# Authentication details
username = ''
password = ''

# Encoding credentials
credentials = base64.b64encode(f'{username}:{password}'.encode()).decode()

# Defining sensor values
sensor_values = {
    "sensor1": 0.5,
    "sensor2": 0.6,
    "sensor3": 0.7
}

# Generating session nonce
session_nonce = secrets.token_hex(32)

# Setting headers with session nonce
headers = {
    'Authorization': f'Basic {credentials}',
    'TrustAPI-Session-Nonce': session_nonce
}

# Making 15 POST requests
for _ in range(15):
    # Building data payload
    data = {"sensor_readings": sensor_values}

    # Making POST request
    response = requests.post(url, json=data, headers=headers)

    # Printing the response
    print(response.text)

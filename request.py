import requests
import json

# Define the URL and payload
url = "http://[IP]/api/sound"
payload = {"sound": "[name of the file in the MELODIES folder without writing .txt]"}

# Convert the payload to JSON format
payload_json = json.dumps(payload)

# Define authentication credentials (if necessary)
nickname = "[nickname]"
password = "[password]"

# Send the POST request with authentication credentials
response = requests.post(url, data=payload_json, auth=(nickname, password))

# Check the response status
if response.status_code == 200:
    print("Request sent successfully.")
else:
    print(f"Error {response.status_code} while sending the request.")

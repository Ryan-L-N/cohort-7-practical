import requests, http

base_url = "http://20.127.202.175:8000"
headers = {
    "Accept": "application/json",
    'X-Base-One-Status': 'EMERGENCY-POWER',
    'X-Username': "chief.engineer",
    'X-Password': "ares-vallis-7",
}
response = requests.get(base_url, headers=headers)

print(f"{response.text}")
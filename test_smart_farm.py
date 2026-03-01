import requests

# ---------- CONFIG ----------
BASE_URL = "http://127.0.0.1:8000/api"  # change if needed
USERNAME = "rwibutso"
PASSWORD = "9090"

# ---------- STEP 1: Get JWT Token ----------
token_url = f"{BASE_URL}/token/"
response = requests.post(token_url, json={"username": USERNAME, "password": PASSWORD})

if response.status_code != 200:
    raise Exception(f"Failed to get token: {response.status_code}, {response.text}")

tokens = response.json()
access_token = tokens["access"]
print("✅ Access token obtained")

headers = {"Authorization": f"Bearer {access_token}"}

# ---------- STEP 2: Get Farms (multi-tenant check) ----------
farms_url = f"{BASE_URL}/farms/"
response = requests.get(farms_url, headers=headers)
print(f"✅ Farms for user {USERNAME}:")
print(response.json())

# ---------- STEP 3: Create a new Farm (auto-owner test) ----------
new_farm_data = {"name": "Test Farm", "location": "Test Location"}
response = requests.post(farms_url, json=new_farm_data, headers=headers)

if response.status_code == 201:
    print("✅ New farm created successfully:")
    print(response.json())
else:
    print(f"❌ Failed to create farm: {response.status_code}, {response.text}")

# ---------- STEP 4: Verify Farm List Again ----------
response = requests.get(farms_url, headers=headers)
print("✅ Updated farm list:")
print(response.json())
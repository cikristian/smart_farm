import requests

# ---------- CONFIG ----------
BASE_URL = ""  # change if needed
USERNAME = ""
PASSWORD = ""  # your real password

# ---------- STEP 1: Get JWT Token ----------
token_url = f"{BASE_URL}/token/"
response = requests.post(token_url, json={"username": USERNAME, "password": PASSWORD})
response.raise_for_status()
access_token = response.json()["access"]
print("✅ Access token obtained")

headers = {"Authorization": f"Bearer {access_token}"}

# ---------- STEP 2: List farms ----------
farms_url = f"{BASE_URL}/farms/"
response = requests.get(farms_url, headers=headers)
print(f"✅ Farms for user {USERNAME}:", response.json())

# ---------- STEP 3: Create a new farm ----------
new_farm_data = {"name": "Updated Test Farm", "location": "New Location"}
response = requests.post(farms_url, headers=headers, json=new_farm_data)
response.raise_for_status()
farm = response.json()
print("✅ New farm created successfully:", farm)

# ---------- STEP 4: Update the farm ----------
farm_id = farm["id"]
update_data = {"name": "Renamed Farm", "location": "Updated Location"}
response = requests.put(f"{farms_url}{farm_id}/", headers=headers, json=update_data)
response.raise_for_status()
print("✅ Farm updated successfully:", response.json())

# ---------- STEP 5: Create a transaction linked to the farm ----------
transactions_url = f"{BASE_URL}/transactions/"
transaction_data = {
    "farm": farm_id,
    "transaction_type": "income",
    "amount": "1000.00",
    "date": "2026-03-01",
    "description": "Initial investment"
}
response = requests.post(transactions_url, headers=headers, json=transaction_data)
response.raise_for_status()
transaction = response.json()
print("✅ Transaction created successfully:", transaction)

# ---------- STEP 6: Delete the farm ----------
response = requests.delete(f"{farms_url}{farm_id}/", headers=headers)
if response.status_code == 204:
    print(f"✅ Farm {farm_id} deleted successfully")
else:
    print(f"❌ Failed to delete farm {farm_id}: {response.status_code}, {response.text}")

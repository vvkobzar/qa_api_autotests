import httpx
from tools.fakers import fake


URL = "http://localhost:8000"

login_payload = {
  "email": fake.email(),
  "password": "string"
}

login_response = httpx.post(f"{URL}/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

print("Login response:", login_response_data)
print("Status Code:", login_response.status_code)


refresh_payload = {
  "refreshToken": login_response_data['token']['refreshToken']
}

refresh_response = httpx.post(f"{URL}/api/v1/authentication/refresh", json=refresh_payload)
refresh_response_data = refresh_response.json()

print("Refresh response:", refresh_response_data)
print("Status Code:", refresh_response.status_code)
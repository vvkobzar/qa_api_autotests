import httpx
from tools.fakers import fake

URL = "http://localhost:8000"

payload = {
  "email": fake.email(),
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

response = httpx.post(f"{URL}/api/v1/users", json=payload)

print(response.status_code)
print(response.json())

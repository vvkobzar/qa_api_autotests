import httpx

response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")

print(response.status_code)
print(response.json())



date = {
    "title": "Новая задача",
    "completed": False,
    "userId": 1
}

response = httpx.post("https://jsonplaceholder.typicode.com/todos", json=date)

print(response.status_code)
print(response.json())



date = {
    "username": "test_user",
    "password": "123456"
}

response = httpx.post("https://httpbin.org/post", data=date)

print(response.status_code)
print(response.json())



headers = {
    "Authorization": "Bearer my_secret_token",
}

response = httpx.get("https://httpbin.org/get", headers=headers)

print(response.request.headers)
print(response.json())



params = {"userId": 1}
response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)

print(response.url)
print(response.json())



files = {
    "files": ("example.txt", open("example.txt", "rb"))
}
response = httpx.post("https://httpbin.org/post", files=files)

print(response.json())



with httpx.Client() as client:
    response_1 = client.get("https://jsonplaceholder.typicode.com/todos/1")
    response_2 = client.get("https://jsonplaceholder.typicode.com/todos/2")

print(response_1.json())
print(response_2.json())



client = httpx.Client(headers={"Authorization": "Bearer my_secret_token"})
response = httpx.get("https://httpbin.org/get")

print(response.json())


try:
    response = httpx.get("https://jsonplaceholder.typicode.com/invalid_url")
    response.raise_for_status()
except httpx.HTTPStatusError as e:
    print(f"Ошибка запроса: {e}")



try:
    response = httpx.get("https://httpbin.ort/delay/5", timeout=2)
except httpx.ReadTimeout:
    print("Запрос превысил лимит времени")
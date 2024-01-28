import requests

print("----------------------------------------hello---------------------------------")
url = 'http://127.0.0.1:8080/api/hello'
data = {'input_string': 'only 3 left'}
response = requests.post(url, json=data)
data2 = response.json()  # Corrected
print(data2)

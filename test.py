import requests

resp = requests.post(
    "http://127.0.0.1:8000/predict",
    json={"text": "You won a free iPhone!"}
)
print("Status:", resp.status_code)
print("Response:", resp.text)

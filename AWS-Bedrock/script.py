import requests

response = requests.post("http://localhost:5000/prompt", json={"prompt": "prompt_text"})

if response.ok:
    print(response.json()["prompt_response"])
else:
    print("Error:", response.text)

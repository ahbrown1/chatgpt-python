import requests
import os

api_endpoint="https://api.openai.com/v1/completions"
api_key = os.getenv('CHATGPT_API_KEY')
model = "text-davinci-003"

prompt = "Write a python script to print Hello"

headers = {
    "Content-Type" : "application/json",
    "Authorization" : f"Bearer {api_key}"
}

request_data = {
    "model" : model,
    "prompt" : prompt,
    "max_tokens" :100,
    "temperature" : 0.5
}


response = requests.post(api_endpoint, 
    headers=headers,
    json=request_data,
)
if response.status_code == 200:

    print(response.json()["choices"][0]["text"])
else:
    print (f"Failed with status code {response.status_code}")
    print(response.text)








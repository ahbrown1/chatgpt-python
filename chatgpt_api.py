import requests
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("prompt", help='prompt to send')
parser.add_argument("filename", help='output file')

args = parser.parse_args()

api_endpoint="https://api.openai.com/v1/completions"
api_key = os.getenv('CHATGPT_API_KEY')
model = "text-davinci-003"

if api_key is None:
    raise Exception("No API key is set ")

#prompt = "Write a python script to print Hello/ Provide only code no text"
prompt = args.prompt

headers = {
    "Content-Type" : "application/json",
    "Authorization" : f"Bearer {api_key}"
}

request_data = {
    "model" : model,
    "prompt" : prompt,
    "max_tokens" :1000,
    "temperature" : 0.5
}


response = requests.post(api_endpoint, 
    headers=headers,
    json=request_data,
)
if response.status_code == 200:

    print(response.json()["choices"][0]["text"])
    with open(f"output/{args.filename}", 'w') as f:
        f.write(response.json()["choices"][0]["text"])
else:
    print(f"Failed with status code {response.status_code}")
    print(response.text)








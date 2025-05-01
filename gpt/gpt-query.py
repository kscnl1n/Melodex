import requests
import sys

def query_gpt_api(message):
    api_url = "https://api.openai.com/v1/engines/gpt-4.1/completions"
    headers = {
        "Authorization": f"Bearer API_KEY",
        "Content-Type": "application/json"
    }
    data = {
        "prompt": message,
        "max_tokens": 100
    }
    response = requests.post(api_url, headers=headers, json=data, verify=False)
    return response.json()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Run as: python3 gpt-query.py <message>")
        print("or whatever the hell your python env variable is, my computer is weird and im to lazy to change it. :)")
        sys.exit(1)
    
    message = " ".join(sys.argv[1:])
    response = query_gpt_api(message)
    print(response)

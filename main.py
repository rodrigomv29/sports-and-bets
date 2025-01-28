import os
import json
from dotenv import load_dotenv
from llamaapi import LlamaAPI

load_dotenv()
api_key = os.getenv("API_KEY")

llama = LlamaAPI(api_key)

api_request_json = {
    "model": "llama3.1-70b",
    "messages": [
        {"role": "user", "content": "Explain the math behind money betting lines and what over/under means?"},
    ], 
}

# Execute the Request
response = llama.run(api_request_json)
try:
    print(json.dumps(response.json(), indent=2))
except:
    print("\n\n\n\n\n " + response.text)

"""
import os
import json
from dotenv import load_dotenv
from llamaapi import LlamaAPI

load_dotenv()
api_key = os.getenv("LLAMA_API_KEY")

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

"""
import sqlite3
def connect_to_db(name):
    conn = None
    try:
        conn = sqlite3.connect(name)
        print(f"Connected to database {name} successfully.")
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
    return conn

if __name__ == "__main__":
    connection = connect_to_db('sports.db')
    print(connection)
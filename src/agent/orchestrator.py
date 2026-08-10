#!/usr/bin/env python3
import requests
import json
import sys
import subprocess
import os

INTENT_MAP = {
    "focus": 1,
    "sleep": 2,
    "silent": 3,
    "normal": 4
}

def ask_llm(prompt):
    tailnet = os.getenv("TAILNET_NAME", "your-tailnet-name.ts.net") 
    url = f"http://ollama-node.{tailnet}:11434/api/generate"
    
    payload = {
        "model": "llama3.2:3b",
        "prompt": f"Respond with ONLY one word from this list: focus, sleep, silent, normal. User says: {prompt}",
        "stream": False
    }
    try:
        response = requests.post(url, json=payload, timeout=30)
        return response.json()["response"].strip().lower()
    except Exception as e:
        print(f"LLM Connection Error: {e}")
        return "normal"

def trigger_android(intent_code):
    print(f"Sending intent code {intent_code} to target...")
    subprocess.run(["python3", "android/mock/mock_listener.py", str(intent_code)])

if __name__ == "__main__":
    user_input = input("What do you want to do? ")
    llm_response = ask_llm(user_input)
    print(f"LLM response: {llm_response}")
    
    if llm_response in INTENT_MAP:
        code = INTENT_MAP[llm_response]
        trigger_android(code)
    else:
        print("Unknown response from LLM. Action aborted.")

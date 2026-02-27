import json
import os

STATE_FILE = "state.json"

def load_state():
    if not os.path.exists(STATE_FILE):
        return {"mode": "basic", "treasury": 0.0, "previous_balance": 0.0}

    with open(STATE_FILE, "r") as f:
        return json.load(f)

def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f)

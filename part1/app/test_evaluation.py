import re
import pytest
from fastapi.testclient import TestClient
from app.main import app 

client = TestClient(app)

test_cases = [
    {
        "name": "Ethereum price",
        "prompt": "What is the current price of Ethereum?",
        "validate": lambda resp: bool(re.search(r"\$?\d{3,5}", resp)),  
    },
    {
        "name": "UEFA Euro 2024 winner",
        "prompt": "Who won the last UEFA Euro final?",
        "validate": lambda resp: any(country in resp for country in ["Spain", "England"]),
    },
    {
        "name": "Eiffel Tower history",
        "prompt": "Tell me about the history of the Eiffel Tower.",
        "validate": lambda resp: "1889" in resp or "Paris" in resp,
    },
    {
        "name": "Math calculation",
        "prompt": "What is 784 divided by 4.7?",
        "validate": lambda resp: bool(re.search(r"\d+\.\d+", resp)),  
    },
    {
        "name": "Bitcoin price",
        "prompt": "What's the current price of Bitcoin?",
        "validate": lambda resp: bool(re.search(r"\$?\d{1,3}(,\d{3})*(\.\d{2})?", resp)),
    },
    {
        "name": "Translate Hello",
        "prompt": "Translate 'Hello' to Spanish.",
        "validate": lambda resp: "Hola" in resp,
    },
    {
        "name": "Capital of France",
        "prompt": "What is the capital of France?",
        "validate": lambda resp: "Paris" in resp,
    }
]

@pytest.mark.parametrize("case", test_cases)
def test_agent_response(case):
    res = client.post("/agent", json={"prompt": case["prompt"]})
    assert res.status_code == 200
    data = res.json()
    assert "response" in data
    assert case["validate"](data["response"]), f"Failed case: {case['name']}"

import requests
from research import fetch_papers
from memory import load_state, save_state
from wallet import get_balance, is_connected

MODEL_NAME = "phi3"

from web3 import Web3

WALLET_ADDRESS = Web3.to_checksum_address("0xa1accdf92fbddc61cde572c4eac6d887ed24e48b")
UPGRADE_THRESHOLD = 0.01  # testnet threshold


def generate(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"]


def summarize_paper(paper, mode):
    if mode == "basic":
        prompt = f"""
Give a short 5 sentence summary of this AI research paper.

Title: {paper['title']}
Abstract: {paper['summary'][:800]}
"""
    else:
        prompt = f"""
Provide deep technical analysis of this AI paper:
- Core idea
- Technical innovation
- Possible limitations
- Future research directions

Title: {paper['title']}
Abstract: {paper['summary'][:1000]}
"""
    return generate(prompt)


# =========================
# LOAD MEMORY
# =========================
state = load_state()

print("🚀 ClawScholar Activated")
print("Previous Mode:", state["mode"])
print("Stored Treasury:", state["treasury"])
print("-" * 50)


# =========================
# CHECK BLOCKCHAIN
# =========================
print("Checking blockchain connection...")

if is_connected():
    print("✅ Connected to Sepolia")

    real_balance = get_balance(WALLET_ADDRESS)
    print("On-chain Balance:", real_balance)

    previous_balance = state.get("previous_balance", 0.0)

    if real_balance > previous_balance:
        received_amount = real_balance - previous_balance
        print("💰 New payment detected!")
        print("Amount received:", received_amount)

        if state["mode"] == "basic" and real_balance >= UPGRADE_THRESHOLD:
            state["mode"] = "advanced"
            print("⚡ Switching to Advanced Mode due to funding.")

    state["treasury"] = real_balance
    state["previous_balance"] = real_balance

else:
    print("❌ Could not connect to Sepolia RPC")

print("-" * 50)
print("Current Treasury:", state["treasury"])
print("Current Mode:", state["mode"])
print("-" * 50)


# =========================
# GENERATE RESEARCH OUTPUT
# =========================
papers = fetch_papers()

if len(papers) > 0:
    paper = papers[0]
    print("📄 Title:", paper["title"])
    print("\nGenerating analysis...\n")

    summary = summarize_paper(paper, state["mode"])
    print(summary)
else:
    print("No papers found.")


# =========================
# SAVE MEMORY
# =========================
save_state(state)
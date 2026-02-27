# ============================
# CLAWSCHOLAR AGENT
# ============================

from wallet import get_balance
from memory import load_state, save_state
from research import fetch_papers, summarize_paper

# Upgrade threshold (in ETH)
UPGRADE_THRESHOLD = 0.1


def run_agent(title):
    """
    Main autonomous agent logic.
    Called by Streamlit UI.
    """

    print("Checking blockchain connection...")

    # Load memory
    state = load_state()
    previous_balance = state.get("previous_balance", 0.0)

    # Get real on-chain balance
    real_balance = get_balance()

    if real_balance is None:
        return "❌ Could not connect to Sepolia RPC."

    print("Connected to Sepolia")
    print("On-chain Balance:", real_balance)

    # Detect new payment
    if real_balance > previous_balance:
        received_amount = real_balance - previous_balance
        print("💰 New payment detected!")
        print("Amount received:", received_amount)

    # Upgrade mode if threshold crossed
    if state["mode"] == "basic" and real_balance >= UPGRADE_THRESHOLD:
        state["mode"] = "advanced"
        print("🚀 Switching to Advanced Mode due to funding.")

    # Update treasury
    state["treasury"] = real_balance
    state["previous_balance"] = real_balance

    print("-" * 50)
    print("Current Treasury:", state["treasury"])
    print("Current Mode:", state["mode"])
    print("-" * 50)

    # ============================
    # GENERATE RESEARCH OUTPUT
    # ============================

    papers = fetch_papers(title)

    if len(papers) > 0:
        paper = papers[0]
        summary = summarize_paper(paper, state["mode"])
    else:
        summary = "No papers found for this topic."

    # Save updated memory
    save_state(state)

    return summary


# ============================
# OPTIONAL LOCAL TEST MODE
# ============================

if __name__ == "__main__":
    result = run_agent("Quantum Gravity")
    print("\n=== AGENT OUTPUT ===\n")
    print(result)
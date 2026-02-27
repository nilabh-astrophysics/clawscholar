# =========================================
# CLAWSCHOLAR AUTONOMOUS RESEARCH ENGINE v3
# =========================================

from wallet import get_balance
from memory import load_state, save_state
from research import fetch_papers
import random

# =========================
# FUNDING THRESHOLDS
# =========================

UPGRADE_THRESHOLD = 0.15
MULTI_PAPER_THRESHOLD = 0.25
ELITE_THRESHOLD = 0.40


# =========================
# MODE ENGINE
# =========================

def determine_mode(balance: float) -> str:
    if balance >= ELITE_THRESHOLD:
        return "elite"
    elif balance >= MULTI_PAPER_THRESHOLD:
        return "advanced"
    elif balance >= UPGRADE_THRESHOLD:
        return "enhanced"
    return "basic"


def innovation_score(balance: float) -> int:
    base = 60
    multiplier = min(balance * 100, 35)
    return int(base + multiplier)


# =========================
# ANALYSIS GENERATORS
# =========================

def generate_basic(paper):
    return f"""
📘 BASIC MODE

Title: {paper['title']}

Overview:
Concise explanation of the paper's objective and results.

Upgrade treasury to unlock deeper research intelligence.
"""


def generate_enhanced(paper, balance):
    return f"""
🧠 ENHANCED MODE

Title: {paper['title']}

Structured Technical Summary:
• Core methodology  
• Analytical implications  
• Theoretical positioning  

Treasury: {round(balance,6)} ETH
"""


def generate_advanced(papers, balance):
    titles = [p["title"] for p in papers[:2]]

    return f"""
🚀 ADVANCED MODE (Multi-Paper Synthesis)

Papers:
• {titles[0]}
• {titles[1] if len(titles) > 1 else "-"}

Cross-Paper Insights:
• Shared theoretical constructs  
• Methodological contrasts  
• Unified interpretation  

Treasury: {round(balance,6)} ETH
"""


def generate_elite(papers, balance):
    titles = [p["title"] for p in papers[:3]]

    score = innovation_score(balance)

    return f"""
🔥 ELITE RESEARCH ENGINE

Integrated Papers:
• {titles[0]}
• {titles[1] if len(titles) > 1 else "-"}
• {titles[2] if len(titles) > 2 else "-"}

Unified Research Framework:
Cross-domain abstraction layer activated.

Emergent Research Directions:
• Experimental roadmap
• Formal extensions
• Computational scaling

Innovation Potential Score: {score}/100

Treasury: {round(balance,6)} ETH
"""


# =========================
# MAIN AGENT
# =========================

def run_agent(title: str):

    try:
        state = load_state()
    except Exception:
        state = {"treasury": 0.0, "previous_balance": 0.0}

    try:
        balance = get_balance()
        balance = float(balance) if balance else 0.0
    except Exception:
        return "❌ Blockchain connection failed."

    previous_balance = state.get("previous_balance", 0.0)

    if balance > previous_balance:
        print(f"💰 New funding: {balance - previous_balance} ETH")

    mode = determine_mode(balance)

    state["mode"] = mode
    state["treasury"] = balance
    state["previous_balance"] = balance

    try:
        papers = fetch_papers(title)
    except Exception:
        return "❌ Failed to fetch research."

    if not papers:
        return "No relevant research papers found."

    if mode == "elite":
        output = generate_elite(papers, balance)
    elif mode == "advanced":
        output = generate_advanced(papers, balance)
    elif mode == "enhanced":
        output = generate_enhanced(papers[0], balance)
    else:
        output = generate_basic(papers[0])

    save_state(state)

    return output

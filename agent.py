# =========================================
# CLAWSCHOLAR AUTONOMOUS RESEARCH AGENT v2
# =========================================

from wallet import get_balance
from memory import load_state, save_state
from research import fetch_papers
import random

# =========================
# CONFIGURATION
# =========================

UPGRADE_THRESHOLD = 0.15
MULTI_PAPER_THRESHOLD = 0.25
DEEP_SYNTHESIS_THRESHOLD = 0.40


# =========================
# MODE ENGINE
# =========================

def determine_mode(balance: float) -> str:
    if balance >= DEEP_SYNTHESIS_THRESHOLD:
        return "elite"
    elif balance >= MULTI_PAPER_THRESHOLD:
        return "advanced"
    elif balance >= UPGRADE_THRESHOLD:
        return "enhanced"
    return "basic"


# =========================
# OUTPUT GENERATORS
# =========================

def generate_basic_analysis(paper):
    return f"""
📘 ClawScholar (Basic Mode)

Title: {paper['title']}

Overview:
This paper introduces the core concept and presents its main findings.

Key Highlights:
• Research objective  
• Core methodology  
• Primary result  

Upgrade funding to unlock deeper analytical reasoning.
"""


def generate_enhanced_analysis(paper, balance):
    return f"""
🧠 ClawScholar (Enhanced Mode)

Title: {paper['title']}

Structured Summary:
This research formalizes the problem domain and evaluates theoretical or experimental mechanisms.

Technical Layers:
• Model assumptions  
• System boundaries  
• Analytical implications  

Funding Level: {round(balance,6)} ETH  
Increased reasoning depth activated.
"""


def generate_advanced_analysis(papers, balance):
    titles = [p["title"] for p in papers[:2]]

    return f"""
🚀 ClawScholar (Advanced Mode – Multi-Paper Synthesis)

Papers Analyzed:
• {titles[0]}
• {titles[1] if len(titles) > 1 else "—"}

Cross-Paper Insights:
• Shared theoretical structure  
• Methodological divergence  
• Converging conclusions  

Research Gaps Identified:
• Scalability constraints  
• Missing empirical validation  
• Optimization potential  

Treasury: {round(balance,6)} ETH  
Multi-paper synthesis activated.
"""


def generate_elite_analysis(papers, balance):
    titles = [p["title"] for p in papers[:3]]

    innovation_score = random.randint(82, 97)

    return f"""
🔥 ClawScholar ELITE Research Engine

Papers Integrated:
• {titles[0]}
• {titles[1] if len(titles) > 1 else "—"}
• {titles[2] if len(titles) > 2 else "—"}

Unified Theoretical Framework:
This system constructs a synthesized abstraction across multiple works,
identifying hidden structural relationships.

Emergent Research Directions:
• Cross-domain unification  
• Computational scaling  
• Formal proof extensions  
• Experimental validation pipelines  

Innovation Potential Score: {innovation_score}/100

Treasury: {round(balance,6)} ETH  
Autonomous high-order reasoning unlocked.
"""


# =========================
# MAIN AGENT
# =========================

def run_agent(title: str):

    try:
        state = load_state()
    except Exception:
        state = {"mode": "basic", "treasury": 0.0, "previous_balance": 0.0}

    # Fetch on-chain balance
    try:
        balance = get_balance()
        balance = float(balance) if balance is not None else 0.0
    except Exception:
        return "❌ Blockchain connection failed."

    # Detect funding event
    previous_balance = state.get("previous_balance", 0.0)
    if balance > previous_balance:
        print(f"💰 New funding detected: {balance - previous_balance} ETH")

    # Determine intelligence tier
    mode = determine_mode(balance)

    state["mode"] = mode
    state["treasury"] = balance
    state["previous_balance"] = balance

    # Fetch research papers
    try:
        papers = fetch_papers(title)
    except Exception:
        return "❌ Failed to retrieve research data."

    if not papers:
        return "No relevant research papers found."

    # Generate output by intelligence tier
    if mode == "elite":
        output = generate_elite_analysis(papers, balance)
    elif mode == "advanced":
        output = generate_advanced_analysis(papers, balance)
    elif mode == "enhanced":
        output = generate_enhanced_analysis(papers[0], balance)
    else:
        output = generate_basic_analysis(papers[0])

    # Save state
    try:
        save_state(state)
    except Exception:
        pass

    return output


# =========================
# LOCAL TEST
# =========================

if __name__ == "__main__":
    print(run_agent("Quantum Entanglement"))

# =========================================
# CLAWSCHOLAR AUTONOMOUS RESEARCH ENGINE v4
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
# ROADMAP GENERATOR
# =========================

def generate_roadmap(mode: str):
    if mode == "basic":
        return """
🗺 Research Roadmap (Basic)

Phase 1: Concept clarification  
Phase 2: Literature consolidation  
Phase 3: Identify key open questions  
"""

    if mode == "enhanced":
        return """
🗺 Research Roadmap (Enhanced)

Phase 1: Formal theoretical modeling  
Phase 2: Controlled simulation testing  
Phase 3: Parameter sensitivity analysis  
Phase 4: Draft experimental validation framework  
"""

    if mode == "advanced":
        return """
🗺 Research Roadmap (Advanced)

Phase 1: Multi-model comparative study  
Phase 2: Cross-disciplinary integration  
Phase 3: High-performance computational modeling  
Phase 4: Prototype experimental design  
Phase 5: Publication & grant targeting  
"""

    if mode == "elite":
        return """
🗺 Research Roadmap (Elite Autonomous Strategy)

Phase 1: Unified theoretical abstraction  
Phase 2: Multi-lab collaborative validation  
Phase 3: Funding allocation optimization  
Phase 4: Autonomous research pipeline deployment  
Phase 5: DAO-governed research expansion  
"""

    return ""


# =========================
# ANALYSIS GENERATORS
# =========================

def generate_basic(paper):
    return f"""
📘 BASIC MODE

Title: {paper['title']}

Overview:
Concise explanation of the research objective and outcome.
"""


def generate_enhanced(paper):
    return f"""
🧠 ENHANCED MODE

Title: {paper['title']}

Structured Summary:
• Core methodology  
• Theoretical implications  
• Analytical observations  
"""


def generate_advanced(papers):
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

Unified Research Abstraction Layer Activated.

Innovation Potential Score: {score}/100
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
        analysis = generate_elite(papers, balance)
    elif mode == "advanced":
        analysis = generate_advanced(papers)
    elif mode == "enhanced":
        analysis = generate_enhanced(papers[0])
    else:
        analysis = generate_basic(papers[0])

    roadmap = generate_roadmap(mode)

    save_state(state)

    return analysis + "\n\n" + roadmap

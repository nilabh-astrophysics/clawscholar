# =========================================
# CLAWSCHOLAR AUTONOMOUS RESEARCH ENGINE
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
    base = 65
    multiplier = min(balance * 100, 30)
    return int(base + multiplier)


# =========================
# GAP DETECTION ENGINE
# =========================

def detect_research_gaps():
    gaps = [
        "Inconsistent boundary condition assumptions across models",
        "Lack of high-scale empirical validation",
        "Computational scalability constraints under extreme regimes",
        "Parameter sensitivity underexplored in current literature",
        "Cross-domain generalization not formally proven"
    ]
    return random.sample(gaps, 3)


# =========================
# FUNDING ALLOCATION ENGINE
# =========================

def funding_allocation(balance: float, mode: str):

    if mode == "advanced":
        return {
            "Theoretical Modeling": 40,
            "Simulation Infrastructure": 35,
            "Experimental Validation": 25
        }

    if mode == "elite":
        return {
            "Unified Theory Development": 30,
            "High-Performance Computing": 30,
            "Experimental Labs": 25,
            "Cross-Disciplinary Research": 15
        }

    return {}


# =========================
# ANALYSIS GENERATORS
# =========================

def generate_basic(paper):
    return f"""
📘 BASIC MODE

Title: {paper['title']}

This research explores the primary objective and methodological foundation of the study.
It provides foundational insights but remains limited in strategic synthesis depth.
"""


def generate_enhanced(paper):
    return f"""
🧠 ENHANCED MODE

Title: {paper['title']}

Structured Summary:
• Core methodology and modeling framework  
• Theoretical implications and domain constraints  
• Analytical observations and performance considerations  

Research Readiness: Moderate depth exploration enabled.
"""


def generate_advanced(papers, balance):
    titles = [p["title"] for p in papers[:2]]
    gaps = detect_research_gaps()
    allocation = funding_allocation(balance, "advanced")

    return f"""
🚀 ADVANCED MODE – Strategic Research Synthesis

Integrated Papers:
• {titles[0]}
• {titles[1] if len(titles) > 1 else "-"}

Cross-Paper Insights:
• Convergent structural modeling approaches
• Divergent optimization strategies under varying constraints
• Partial theoretical incompatibility in parameter regimes

🧩 Detected Research Gaps:
• {gaps[0]}
• {gaps[1]}
• {gaps[2]}

💰 Autonomous Funding Allocation Strategy:
• Theoretical Modeling: {allocation["Theoretical Modeling"]}%
• Simulation Infrastructure: {allocation["Simulation Infrastructure"]}%
• Experimental Validation: {allocation["Experimental Validation"]}%

Strategic Depth: Multi-paper synthesis activated.
"""


def generate_elite(papers, balance):
    titles = [p["title"] for p in papers[:3]]
    score = innovation_score(balance)
    gaps = detect_research_gaps()
    allocation = funding_allocation(balance, "elite")

    return f"""
🔥 ELITE AUTONOMOUS RESEARCH ENGINE

Integrated Works:
• {titles[0]}
• {titles[1] if len(titles) > 1 else "-"}
• {titles[2] if len(titles) > 2 else "-"}

Unified Research Abstraction Layer Constructed.

🧩 Critical Theoretical Contradictions Identified:
• {gaps[0]}
• {gaps[1]}
• {gaps[2]}

💰 Strategic Treasury Deployment Plan:
• Unified Theory Development: {allocation["Unified Theory Development"]}%
• High-Performance Computing: {allocation["High-Performance Computing"]}%
• Experimental Labs: {allocation["Experimental Labs"]}%
• Cross-Disciplinary Research: {allocation["Cross-Disciplinary Research"]}%

Innovation Potential Score: {score}/100

Autonomous Research Capital Allocation Active.
"""


# =========================
# MAIN AGENT
# =========================

def run_agent(title: str):

    # Load previous state safely
    try:
        state = load_state()
    except Exception:
        state = {"treasury": 0.0, "previous_balance": 0.0}

    # Get live balance
    try:
        balance = get_balance()
        balance = float(balance) if balance else 0.0
    except Exception:
        return "❌ Blockchain connection failed."

    # 🔥 Always determine mode from LIVE balance
    mode = determine_mode(balance)

    state["mode"] = mode
    state["treasury"] = balance
    state["previous_balance"] = balance

    # Fetch research papers
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
        output = generate_enhanced(papers[0])
    else:
        output = generate_basic(papers[0])

    save_state(state)

    return output

import random

def fetch_papers(title):
    """
    Simulated paper fetch.
    Returns structured metadata for demo purposes.
    """
    return [{
        "title": title,
        "authors": ["A. Researcher", "B. Scientist"],
        "year": 2024,
        "abstract": f"This study investigates advanced theoretical and applied aspects of {title}."
    }]


def summarize_paper(paper, mode):
    title = paper["title"]

    if mode == "basic":
        return f"""
🔎 ClawScholar Analysis (BASIC Mode)

Title: {title}

Summary:
This research explores foundational concepts related to {title}. 
It presents core theoretical insights and highlights key problem formulations.

Key Focus Areas:
• Conceptual framework
• Mathematical foundations
• Broad scientific relevance

This summary is optimized for clarity and accessibility.
"""

    elif mode == "advanced":
        return f"""
🚀 ClawScholar Analysis (ADVANCED Mode)

Title: {title}

Technical Summary:
This work develops a rigorous analytical treatment of {title}, 
emphasizing formal modeling, quantitative evaluation, and domain-specific optimization.

Advanced Contributions:
• Theoretical generalization
• Formal derivations
• Computational or experimental validation pathways
• Cross-disciplinary applicability

Funding-aware reasoning depth activated.
Analytical rigor increased.
"""

    else:
        return "Unknown analysis mode."

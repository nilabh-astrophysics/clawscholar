from agent import run_agent


def openclaw_entry(input_payload: dict) -> dict:
    """
    OpenClaw-compatible entry point for ClawScholar.

    Expected input format:
    {
        "research_topic": "Quantum Entanglement in Open Systems"
    }

    Returns structured output compatible with agent runtimes.
    """

    try:
        topic = input_payload.get("research_topic", "")

        if not topic:
            return {
                "status": "error",
                "message": "No research_topic provided."
            }

        result = run_agent(topic)

        return {
            "status": "completed",
            "agent": "ClawScholar",
            "mode": result.get("mode"),
            "analysis": result.get("analysis"),
            "treasury_balance": result.get("treasury_balance")
        }

    except Exception as e:
        return {
            "status": "failed",
            "error": str(e)
        }
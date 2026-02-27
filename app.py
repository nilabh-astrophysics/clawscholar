import streamlit as st
from agent import run_agent
from wallet import get_balance
from memory import load_state

# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(
    page_title="ClawScholar",
    layout="centered"
)

st.title("🧠 ClawScholar")
st.subheader("Autonomous Self-Funding Scientific AI Agent")
st.markdown("---")

# ---------------------------
# On-Chain Status
# ---------------------------
st.header("🔗 On-Chain Status")

# Safe balance fetch
balance_display = "Not Connected"

try:
    balance = get_balance()

    if balance is not None:
        balance = float(balance)
        balance_display = round(balance, 6)
    else:
        balance_display = "Unavailable"

except Exception:
    balance_display = "RPC Error"

# Safe state load
# Dynamic mode detection based on balance
try:
    balance = get_balance()
    balance = float(balance) if balance is not None else 0.0
except Exception:
    balance = 0.0

if balance >= 0.15:   # your demo threshold
    mode_display = "advanced"
else:
    mode_display = "basic"

st.metric("Wallet Balance (Sepolia ETH)", round(balance, 6))
st.metric("Current Mode", mode_display)

st.markdown("---")

# ---------------------------
# Research Section
# ---------------------------
st.header("📚 Research Analysis")

paper_title = st.text_input("Enter Research Paper Title")

if st.button("Run ClawScholar"):
    if not paper_title:
        st.warning("Please enter a title.")
    else:
        try:
            with st.spinner("Analyzing..."):
                output = run_agent(paper_title)

            st.success("Analysis Complete")
            st.write(output)

        except Exception as e:
            st.error("Agent execution failed.")
            st.caption("Check RPC / Ollama / dependencies.")

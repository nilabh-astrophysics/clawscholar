import streamlit as st
from agent import run_agent
from wallet import get_balance
from memory import load_state

WALLET_ADDRESS = "0xa1aCcdF92FBDdc61cDe572C4EAC6D887ED24e48b"

st.set_page_config(page_title="ClawScholar", layout="centered")

st.title("🧠 ClawScholar")
st.subheader("Autonomous Self-Funding Scientific AI Agent")

st.markdown("---")

# Blockchain Status
st.header("🔗 On-Chain Status")

balance = get_balance()
state = load_state()

st.metric("Wallet Balance (Sepolia ETH)", round(balance, 6))
st.metric("Current Mode", state["mode"])

st.markdown("---")

# Run Agent
st.header("📚 Research Analysis")

paper_title = st.text_input("Enter Research Paper Title")

if st.button("Run ClawScholar"):
    if paper_title:
        with st.spinner("Analyzing..."):
            output = run_agent(paper_title)
        st.success("Analysis Complete")
        st.write(output)
    else:
        st.warning("Please enter a title.")

import streamlit as st
from agent import run_agent
from wallet import get_balance
from memory import load_state

st.set_page_config(page_title="ClawScholar", layout="centered")

st.title("🧠 ClawScholar")
st.markdown("### Autonomous Research Capital Engine")
st.markdown(
    "ClawScholar detects research gaps, synthesizes literature, "
    "and allocates blockchain treasury for scientific innovation."
)

st.markdown("---")

# =========================
# SAFE BALANCE FETCH
# =========================

balance_display = "Unavailable"
balance_value = 0.0

try:
    balance = get_balance()
    if balance is not None:
        balance_value = float(balance)
        balance_display = round(balance_value, 6)
except Exception:
    balance_display = "RPC Error"

# =========================
# SAFE STATE LOAD
# =========================

try:
    state = load_state()
    mode_display = state.get("mode", "basic")
except Exception:
    mode_display = "basic"

st.markdown("## 🔗 On-Chain Status")
st.metric("Wallet Balance (Sepolia ETH)", balance_display)
st.metric("Current Mode", mode_display.upper())

st.markdown("### 💰 Treasury Intelligence")

if isinstance(balance_display, float):
    if balance_value >= 0.40:
        st.success("Elite Research Capital Capacity Activated")
    elif balance_value >= 0.25:
        st.info("Advanced Multi-Paper Synthesis Enabled")
    elif balance_value >= 0.15:
        st.warning("Enhanced Analytical Capacity")
    else:
        st.warning("Basic Analytical Capacity")

st.markdown("---")

# =========================
# RESEARCH INPUT
# =========================

st.header("📚 Research Analysis")

title = st.text_input("Enter Research Paper Title")

if st.button("Run ClawScholar"):

    if not title:
        st.warning("Please enter a research title.")
    else:
        with st.spinner("Analyzing research ecosystem..."):
            result = run_agent(title)

        st.success("Autonomous Analysis Complete")

        st.markdown(result)

        # Depth Indicator
        st.markdown("### 📊 Intelligence Depth")

        if mode_display == "elite":
            st.progress(100)
        elif mode_display == "advanced":
            st.progress(75)
        elif mode_display == "enhanced":
            st.progress(50)
        else:
            st.progress(25)

        if "Innovation Potential Score" in result:
            st.markdown("### 🚀 Innovation Index")
            st.metric("Projected Innovation Impact", "High")

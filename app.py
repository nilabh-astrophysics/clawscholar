import streamlit as st
from agent import run_agent
from wallet import get_balance

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
# LIVE MODE CALCULATION
# =========================

if isinstance(balance_display, float):
    if balance_value >= 0.40:
        mode_display = "elite"
    elif balance_value >= 0.25:
        mode_display = "advanced"
    elif balance_value >= 0.15:
        mode_display = "enhanced"
    else:
        mode_display = "basic"
else:
    mode_display = "basic"

# =========================
# UI DISPLAY
# =========================

st.markdown("## 🔗 On-Chain Status")
st.metric("Wallet Balance (Sepolia ETH)", balance_display)
st.metric("Current Mode", mode_display.upper())

with st.expander("ℹ️ Mode Thresholds"):
    st.write("""
    BASIC: < 0.15 ETH  
    ENHANCED: 0.15 – 0.249 ETH  
    ADVANCED: 0.25 – 0.399 ETH  
    ELITE: ≥ 0.40 ETH  

    Mode upgrades automatically as treasury increases.
    """)

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

st.markdown("### 📊 Intelligence Depth")

if mode_display == "elite":
    st.progress(100)
elif mode_display == "advanced":
    st.progress(75)
elif mode_display == "enhanced":
    st.progress(50)
else:
    st.progress(25)

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

        if "Innovation Potential Score" in result:
            st.markdown("### 🚀 Innovation Index")
            st.metric("Projected Innovation Impact", "High")

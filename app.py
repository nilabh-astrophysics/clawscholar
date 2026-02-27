import streamlit as st
import pandas as pd
from wallet import get_balance
from agent import run_agent, determine_mode

st.set_page_config(page_title="ClawScholar", layout="wide")

st.title("🧠 ClawScholar")
st.subheader("Autonomous Self-Funding Scientific AI Agent")

# =========================
# TREASURY DASHBOARD
# =========================

try:
    balance = get_balance()
    balance = float(balance) if balance else 0.0
except Exception:
    balance = 0.0

mode = determine_mode(balance)

col1, col2 = st.columns(2)

col1.metric("Treasury (Sepolia ETH)", round(balance, 6))
col2.metric("Intelligence Tier", mode.upper())

# =========================
# CAPABILITY SCALING CHART
# =========================

tiers = {
    "basic": 1,
    "enhanced": 2,
    "advanced": 3,
    "elite": 4
}

data = pd.DataFrame({
    "Capability Level": list(tiers.values())
}, index=list(tiers.keys()))

st.markdown("### 📈 Intelligence Scaling")
st.bar_chart(data)

if mode == "elite":
    st.success("🔥 ELITE Research Engine Active")
elif mode == "advanced":
    st.success("🚀 Advanced Multi-Paper Mode Active")
elif mode == "enhanced":
    st.info("🧠 Enhanced Mode Active")
else:
    st.warning("🔹 Basic Mode")

st.markdown("---")

# =========================
# RESEARCH SECTION
# =========================

st.header("📚 Research Analysis")

title = st.text_input("Enter Research Paper Topic")

if st.button("Run ClawScholar"):
    with st.spinner("ClawScholar is thinking..."):
        result = run_agent(title)
        st.success("Analysis Complete")
        st.markdown(result)

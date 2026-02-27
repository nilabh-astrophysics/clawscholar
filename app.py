import streamlit as st
import pandas as pd
from wallet import get_balance
from agent import run_agent, determine_mode

st.set_page_config(page_title="ClawScholar", layout="wide")

st.title("🧠 ClawScholar")
st.subheader("Autonomous Self-Funding Scientific AI Research Engine")

# =========================
# TREASURY DASHBOARD
# =========================

try:
    balance = get_balance()
    balance = float(balance) if balance else 0.0
except:
    balance = 0.0

mode = determine_mode(balance)

col1, col2 = st.columns(2)

col1.metric("Treasury (Sepolia ETH)", round(balance, 6))
col2.metric("Intelligence Tier", mode.upper())

# =========================
# SCALING VISUALIZATION
# =========================

tiers = ["basic", "enhanced", "advanced", "elite"]
levels = [1, 2, 3, 4]

df = pd.DataFrame({"Capability Level": levels}, index=tiers)

st.markdown("### 📈 Intelligence Scaling Chart")
st.bar_chart(df)

if mode == "elite":
    st.success("🔥 ELITE Autonomous Research Mode Active")
elif mode == "advanced":
    st.success("🚀 Advanced Multi-Paper Mode Active")
elif mode == "enhanced":
    st.info("🧠 Enhanced Reasoning Mode Active")
else:
    st.warning("🔹 Basic Mode")

st.markdown("---")

# =========================
# RESEARCH EXECUTION
# =========================

st.header("📚 Research Analysis & Roadmap")

title = st.text_input("Enter Research Topic")

if st.button("Run ClawScholar"):
    with st.spinner("ClawScholar is analyzing and generating roadmap..."):
        result = run_agent(title)
        st.success("Autonomous Analysis Complete")
        st.markdown(result)

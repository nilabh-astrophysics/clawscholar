

\# 🧠 ClawScholar  

\## Autonomous Self-Funding Scientific AI Agent

Built for SURGE × OpenClaw Hackathon 2026



ClawScholar is an AI research agent that owns a blockchain wallet, monitors its own on-chain funding, and dynamically upgrades its intelligence level based on economic input.



It combines:



\* 🧠 Local AI inference (Ollama)

\* 🔗 Web3 wallet integration (Sepolia testnet)

\* 💰 On-chain payment detection

\* 🗂 Persistent memory (JSON state)

\* 📄 Research summarization + advanced analysis



This project demonstrates a new class of AI systems: \*\*economically autonomous agents\*\*.



---



\## 🚀 Vision



Traditional AI tools respond to prompts.



ClawScholar goes further.



It:



\* Owns a wallet

\* Detects real blockchain payments

\* Tracks its treasury

\* Upgrades intelligence mode automatically

\* Persists its internal state



This is a prototype for \*\*self-funding scientific AI entities\*\*.



---



\## 🏗 Architecture



```

User → ClawScholar Agent → Research Analysis

&nbsp;                        ↓

&nbsp;                   Web3 Wallet

&nbsp;                        ↓

&nbsp;               On-chain Balance Check

&nbsp;                        ↓

&nbsp;             Intelligence Mode Upgrade

&nbsp;                        ↓

&nbsp;                  Persistent Memory

```



---



\## ⚙️ Core Features



\### 1️⃣ Research Intelligence



\* Simplifies complex research papers

\* Generates structured analysis

\* Produces advanced output when treasury threshold is reached



\### 2️⃣ Blockchain Integration



\* Connects to Ethereum Sepolia

\* Reads real wallet balance

\* Detects new incoming payments

\* Updates internal treasury



\### 3️⃣ Autonomous Mode Switching



\* Basic Mode → Lightweight summaries

\* Advanced Mode → Deep technical analysis

\* Mode upgrade triggered by funding



\### 4️⃣ Persistent State



Stored in `state.json`:



```json

{

&nbsp; "mode": "advanced",

&nbsp; "treasury": 0.172,

&nbsp; "previous\_balance": 0.172

}

```



The agent remembers its financial history.



---



\## 📂 Project Structure



```

clawscholar/

│

├── agent.py        # Main autonomous agent logic

├── wallet.py       # Web3 balance reader

├── memory.py       # Persistent state manager

├── research.py     # AI summarization module

├── requirements.txt

└── README.md

```



---



\## 🔧 Installation



\### 1️⃣ Clone repository



```

git clone https://github.com/nilabh-astrophysics/clawscholar.git

cd clawscholar

```



---



\### 2️⃣ Install dependencies



```

pip install -r requirements.txt

```



---



\### 3️⃣ Install Ollama



Download from:



\[https://ollama.com](https://ollama.com)



Then pull a model:



```

ollama pull phi3

```



---



\## ▶️ Run the Agent



```

python agent.py

```



You should see:



```

Checking blockchain connection...

✅ Connected to Sepolia

On-chain Balance: 0.17214706

New payment detected!

Upgrading Intelligence Mode...

```



---



\## 🔗 Blockchain Setup



The agent connects to:



\* Ethereum Sepolia Testnet

\* A wallet address defined inside `agent.py`

\* RPC endpoint via Web3



When balance increases:



\* Treasury updates

\* Mode changes

\* Analysis depth increases



---



\## 🧪 Example Output



\*\*Basic Mode\*\*



> Simple summary of research paper in accessible language.



\*\*Advanced Mode\*\*



> Structured technical breakdown with deeper reasoning.



---



\## 🧩 Why This Matters



ClawScholar demonstrates:



\* AI agents can own wallets

\* AI can respond to economic signals

\* Funding can dynamically influence intelligence

\* Agents can persist memory across sessions



This architecture hints toward:



\* Autonomous digital researchers

\* Self-funding AI services

\* Decentralized agent ecosystems



---



\## 🌍 Future Work



\* Multi-agent collaboration

\* On-chain micropayments

\* Decentralized deployment

\* Web interface dashboard

\* Token-gated intelligence tiers



---



\## 🏆 Hackathon Submission Category



Autonomous AI × Web3 Integration

Self-Funding Intelligent Agent Prototype



---



\## 📜 License



MIT License



---





ClawScholar is not just an AI assistant.

It is an economically aware digital research entity.

Intelligence that evolves with value.






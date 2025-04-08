
# 🧠 MSE Insights Copilot
*Empowering Kenyan Micro & Small Enterprises (MSEs) with AI-powered financial insights from M-Pesa and Microsoft Fabric.*

---

## 🚀 Overview
**MSE Insights Copilot** is a practical, end-to-end analytics and AI solution tailored for Kenyan micro and small enterprises. It helps business owners unlock financial insights from everyday mobile money (M-Pesa) transactions, visualize key performance metrics, and interact with their data using a chatbot – all powered by **Microsoft Fabric** and **Azure AI**.

> 💼 **Designed to help business owners answer:**
- “Where is my money going?”
- “Which day is my best for income?”
- “How can I improve profits?”

---

## 📥 Initial App Interface
Below is the homepage view when the app starts. Users are prompted to upload their M-Pesa CSV file to begin analysis.

![Upload Interface](screenshots/Screenshot(498).png)

---

## 🧩 Features

| Feature                  | Description                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| 💸 Income vs Expense Summary | Visual comparison of inflows and outflows using M-Pesa data.                |
| 📈 Daily Cash Flow Trends    | Auto-generated line chart for daily financial health.                      |
| 🧾 Top KPIs                  | Instant view of key financial metrics: profit margin, daily income, etc.    |
| 🧠 AI Copilot Assistant      | Ask natural-language questions like “How did I perform this week?”         |
| 🔍 Semantic Search           | Find specific transactions using AI-enhanced embedding search.             |

---

## 🧪 Tech Stack

| Tool / Service           | Role in the Solution                                                        |
|--------------------------|-----------------------------------------------------------------------------|
| Microsoft Fabric         | Data integration, storage (OneLake), and Power BI dashboard.                |
| Azure OpenAI (GPT-4o)    | Chatbot assistant and insight summarization.                                |
| Azure OpenAI Embeddings  | Vector search for transaction similarity.                                   |
| Streamlit                | Frontend web app for uploading M-Pesa CSVs and interacting with insights.   |
| Python + Pandas          | Data processing and financial calculations.                                 |

---

## 🔍 Microsoft Fabric Lakehouse View
All uploaded M-Pesa transactions are stored in the `mpesa_cleaned` table inside a Microsoft Fabric Lakehouse.

![Lakehouse Data Table](screenshots/Screenshot(497).png)

---

## ⚙️ Eventhouse System Overview
Ingested telemetry and analytics events are stored in an Eventhouse, making them accessible for KQL querying and real-time analysis.

![Eventhouse in Microsoft Fabric](screenshots/Screenshot(496).png)

---

## 🗃️ Fabric Workspace Structure
This shows the full Microsoft Fabric workspace setup including lakehouses, Eventhouses, Power BI reports, and notebooks.

![Fabric Workspace Structure](screenshots/Screenshot(495).png)

---

## 📊 Power BI Financial Dashboard
This report visualizes M-Pesa transactions grouped by date and transaction type, providing a breakdown of inflow vs outflow.

![Power BI Dashboard](screenshots/Screenshot(494).png)

---

## 🛠️ Local Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/mse-insights-copilot.git
cd mse-insights-copilot
```

### 2. Create a .env File
```bash
API_KEY=your_azure_openai_api_key
ENDPOINT_URL=https://your-azure-endpoint
API_VERSION=2023-09-01-preview
EMBEDDING_MODEL=text-embedding-ada-002-kenya-hack
GPT_MODEL=gpt-4o-kenya-hack
```

### 3. Install Dependencies
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 4. Run the Streamlit App
```bash
streamlit run dashboard.py
```

---

## 📦 Final Fabric Artifacts
Final integrated artifacts including eventhouse, lakehouse, semantic models, and Power BI reports ready for deployment.

![Final Fabric Deployment Resources](screenshots\Screenshot(493).png)

---


## 📢 Contributors & Acknowledgments
This project was developed as part of the Microsoft Fabric + Azure AI Hackathon challenge.

---

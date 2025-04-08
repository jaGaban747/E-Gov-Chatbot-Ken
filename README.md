
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

## 📷 Key Visuals and Explanations

### 📊 Power BI Dashboard Screenshot
![Power BI Dashboard](./screenshots/Screenshot_494.png)

**Purpose:**  
Shows overall business performance — monthly trends, income, expenses, and transaction summaries. Built in Power BI connected to Fabric Lakehouse.

---

### 🧠 AI Copilot Chat Interface
![Chatbot UI](./screenshots/Screenshot_495.png)

**Purpose:**  
User can ask questions like “What was my highest expense last month?” and get AI-generated answers using Azure OpenAI.

---

### 📥 Streamlit Upload Page
![Upload CSV](./screenshots/Screenshot_496.png)

**Purpose:**  
User uploads M-Pesa CSV file with transaction records to generate financial insights on-the-fly.

---

### 🔍 Semantic Search Demo
![Semantic Search](./screenshots/Screenshot_497.png)

**Purpose:**  
Search similar transactions using AI embeddings — for example, "all payments to suppliers" or "related customer refunds".

---

## 🛠️ Local Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/mse-insights-copilot.git
cd mse-insights-copilot
```

### 2. Create a `.env` File
```env
API_KEY=your_azure_openai_api_key
ENDPOINT_URL=https://your-proxy-endpoint
API_VERSION=2023-09-01-preview
EMBEDDING_MODEL=text-embedding-ada-002-kenya-hack
GPT_MODEL=gpt-4o-kenya-hack
```

### 3. Install Dependencies
```bash
python -m venv venv
source  venv\Scriptsctivate
pip install -r requirements.txt
```

### 4. Run the Streamlit App
```bash
streamlit run dashboard.py
```

---

## 📝 Documentation Notes

- All embeddings are stored in Eventhouse (Microsoft Fabric Lakehouse)
- Semantic search is powered by Azure OpenAI Embeddings (text-embedding-ada-002-kenya-hack)
- The chatbot uses Azure OpenAI’s GPT-4o model for contextual business insights
- Streamlit acts as the unified frontend for interaction, upload, search, and analysis

---


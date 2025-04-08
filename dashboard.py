# dashboard.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from ai.chatbot import chat_with_ai

st.set_page_config(page_title="MSE Insights Copilot", layout="wide")
st.title("📊 MSE Insights Copilot")

# File uploader
uploaded_file = st.file_uploader("Upload your M-Pesa CSV file", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    df.columns = [col.lower().strip() for col in df.columns]

    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"])
    else:
        st.error("❌ Column 'date' not found in uploaded file.")
        st.stop()

    # Preview raw data
    st.subheader("📄 Raw Data Preview")
    st.dataframe(df.head())

    # Normalize expected columns
    if "amount" in df.columns and "direction" in df.columns:
        df["amount"] = pd.to_numeric(df["amount"], errors="coerce").fillna(0)
        df["direction"] = df["direction"].str.title()
        df["date_only"] = df["date"].dt.date
    else:
        st.error("❌ Required columns 'amount' and 'direction' are missing.")
        st.stop()

    # ✅ FINANCIAL KPIs SECTION
    st.subheader("📈 Financial KPIs")

    total_in = df[df["direction"] == "In"]["amount"].sum()
    total_out = df[df["direction"] == "Out"]["amount"].sum()
    profit_margin = total_in - total_out
    avg_cash = df.groupby("date_only")["amount"].sum().mean()
    top_expense = df[df["direction"] == "Out"].groupby("transaction_type")["amount"].sum().idxmax()

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("💰 Total Income", f"KES {total_in:,.2f}")
    col2.metric("💸 Total Expenses", f"KES {total_out:,.2f}")
    col3.metric("📊 Profit Margin", f"KES {profit_margin:,.2f}")
    col4.metric("📆 Avg Daily Cash Flow", f"KES {avg_cash:,.2f}")
    st.caption(f"🧾 Top Expense Category: **{top_expense}**")

    # ✅ AI INSIGHTS SECTION
    st.subheader("🧠 AI Business Insight")
    try:
        ai_question = (
            "Analyze the overall financial performance from the data below. "
            f"Income: {total_in}, Expenses: {total_out}, Avg Daily Cash: {avg_cash:.2f}, Top Expense: {top_expense}."
            " Give a simple summary for a small business owner in Kenya."
        )
        ai_answer = chat_with_ai(ai_question)
        st.success(ai_answer)
    except Exception as e:
        st.error(f"⚠️ Failed to get AI insight: {e}")

    # ✅ INCOME VS EXPENSE CHART
    st.subheader("💸 Income vs Expense Summary")
    summary = df.groupby("direction")["amount"].sum()
    st.bar_chart(summary)

    # ✅ DAILY CASH FLOW
    st.subheader("📈 Daily Cash Flow")
    df_grouped = df.groupby(["date_only", "direction"])["amount"].sum().unstack().fillna(0)
    st.line_chart(df_grouped)

    # ✅ AI CHATBOT Q&A
    st.subheader("🤖 Ask AI About Your M-Pesa Data")
    user_question = st.text_input("Ask a business question", placeholder="e.g. What were my top expenses last month?")
    if st.button("Submit"):
        sample_text = f"Analyze this M-Pesa data:\n{df_grouped.tail().to_string()}\nUser question: {user_question}"
        ai_response = chat_with_ai(sample_text)
        st.success(ai_response)
else:
    st.info("📤 Please upload your M-Pesa CSV file to begin.")

from pathlib import Path
import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

# --- Paths ---
DB_PATH = Path(__file__).parents[1] / "data" / "processed" / "full_data.db"
SQL_DIR = Path(__file__).parents[1] / "sql"

# --- Load SQL Query ---
def load_query(name):
    with open(SQL_DIR / f"{name}.sql", "r", encoding="utf-8") as f:
        return f.read()

# --- Run Query ---
def run_query(query):
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

# --- App Layout ---
st.set_page_config(page_title="Ecom Insights", page_icon="📦", layout="wide")

st.title("📊 E-Commerce Analytics Dashboard")
st.markdown("Gain insight into revenue, product performance, and customer behavior.")
st.markdown("---")

# --- sidebar filters with defaults ---
st.sidebar.header("📅 Filter Options")
months = df_orders["order_date"].dt.to_period("M").astype(str).unique()
selected_months = st.sidebar.multiselect("Select Months", months, default=months[-3:])


# --- Revenue Overview ---
st.subheader("💰 Revenue Overview")
query = load_query("revenue_overview")
df_rev = run_query(query)
st.dataframe(df_rev)

# --- Top Products ---
st.subheader("🏆 Top Selling Products")
query = load_query("top_products")
df_top = run_query(query)
fig = px.bar(df_top, x="product_name", y="revenue", text="revenue")
st.plotly_chart(fig, use_container_width=True)

# Add more sections as needed...

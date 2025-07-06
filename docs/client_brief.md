```markdown
# 📊 E-Commerce Sales & Customer Insights Dashboard

A freelance-style data analysis project simulating work for an e-commerce client (Elara & Co). This project delivers deep insights into sales trends, customer behavior, and product performance — from raw data to executive report and interactive dashboard.

> 🎯 Built for real-world freelance showcasing — clear goals, structured delivery, business value, and visual storytelling.

---

## 🔍 Project Summary

Elara & Co, a fictional home decor brand, wanted to understand:

- How are our sales evolving month-over-month?
- Which products and customer segments are driving revenue?
- What is our retention rate, and how can we improve it?
- Can we identify repeat customers or high-value profiles?

This project answers those questions with in-depth analysis, modeling, and polished deliverables.

---

## 📦 Deliverables

| Deliverable                  | Description                                        |
|------------------------------|----------------------------------------------------|
| ✅ Executive Summary         | Non-technical PDF with insights + recommendations |
| ✅ Streamlit Dashboard       | Interactive web app with filters and KPIs         |
| ✅ Clean Jupyter Notebooks   | For EDA, modeling, and reporting                  |
| ✅ Utility Scripts           | Modular, reusable Python utilities                |
| ✅ GitHub Repo (this)        | Production-ready structure                        |

---

## 🧠 Key Insights

- 📈 Monthly sales increased by **35%** YoY, but high return rates in Q4
- 🛍️ **20% of customers** drive **80% of revenue**
- 🎯 RFM segmentation reveals untapped **loyalist group** for re-engagement
- 💰 Average Order Value is **25% higher** in Western US customers
- 📉 Highest churn rate in single-purchase, low-discount buyers

---

## 🚀 Live Dashboard

> 🧪 Try the live dashboard:
[🔗 Streamlit Cloud App](https://your-streamlit-app-link.com)

- Filter by month, category, region
- See top products, repeat purchase trends
- View customer segments and retention metrics

---

## 🗂 Project Structure

```

project-freelance-ecom/
├── data/            # raw and processed CSVs
├── notebooks/       # clean, readable notebooks
├── dashboard/       # Streamlit app
├── src/utils/       # cleaning, EDA, plotting modules
├── reports/         # PDF summary, figures
├── docs/            # client brief, notes
└── README.md        # ← this file

````

---

## ⚙️ Tech Stack

- 🐍 Python 3.10
- 🧪 Pandas, NumPy, Seaborn, Matplotlib
- 📊 Scikit-learn, Plotly
- 🧼 Streamlit (for dashboard)
- 💼 Markdown, Excel (optional export)

---

Notebooks workflow 
notebooks/
├── 01-load-orders.ipynb      # Clean + enrich `orders`
├── 02-customer-eda.ipynb     # Join + explore `customers`
├── 03-product-analysis.ipynb # Category trends, revenue
├── 04-returns-analysis.ipynb # Refund rate, patterns
├── 05-campaign-impact.ipynb  # Marketing ROI
├── 06-reviews-sentiment.ipynb # Ratings & text review mining



---

## 📁 Data Sources

- `orders.csv`: transactions and sales
- `customers.csv`: user info
- `products.csv`: SKUs and categories
- `returns.csv`: refunds and reasons

Data is anonymized to simulate a real client project. Original structure modeled after [Shopify-like datasets](https://www.kaggle.com/datasets?search=shopify+sales).

---

## 💼 Freelance Simulation Notes

This project was executed as a **freelance case study**, with:
- A simulated client brief
- Defined deliverables and timelines
- Business-oriented insights
- Reusable tools for future projects

📁 See [`docs/client_brief.md`](docs/client_brief.md)

---

## ✅ How to Run Locally

```bash
# 1. Clone this repo
git clone https://github.com/your-username/project-freelance-ecom.git
cd project-freelance-ecom

# 2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run dashboard (optional)
cd dashboard
streamlit run app.py
````

---

## 📌 Author

**Mashel Odera**
Freelance Data Analyst | [LinkedIn](https://linkedin.com/in/mashelodera) | [Portfolio](https://yourportfolio.com)
📫 *Let’s work together on your next data project.*

---

## 📄 License

This project is for educational and portfolio purposes only. You may fork it for your own learning or freelance showcase.


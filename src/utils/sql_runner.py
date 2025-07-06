import os
import sqlite3
import pandas as pd
from pathlib import Path

# Path setup
sql_dir = Path("../sql")
db_path = Path("../data/processed/full_data.db")
conn = sqlite3.connect(db_path)

# Load all .sql files into a dict
queries = {}
for sql_file in sql_dir.glob("*.sql"):
    with open(sql_file, "r", encoding="utf-8") as f:
        queries[sql_file.stem] = f.read()

# Run queries and store results
results = {}
for name, query in queries.items():
    try:
        results[name] = pd.read_sql_query(query, conn)
        print(f"✅ Ran: {name}")
    except Exception as e:
        print(f"❌ Error in {name}: {e}")

conn.close()

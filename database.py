# database.py
import sqlite3

def init_db():
    conn = sqlite3.connect("queries.db")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS queries (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    case_type TEXT,
                    case_number TEXT,
                    filing_year TEXT,
                    details TEXT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()

def log_query(case_type, case_number, filing_year, details):
    conn = sqlite3.connect("queries.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO queries(case_type, case_number, filing_year, details) VALUES (?, ?, ?, ?)",
                (case_type, case_number, filing_year, str(details)))
    conn.commit()
    conn.close()

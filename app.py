from flask import Flask
import psycopg2
import os
import time

app = Flask(__name__)

def get_conn():
    return psycopg2.connect(
        host="db",
        dbname="practicedb",
        user="practiceuser",
        password="practicepass"
    )

@app.route("/")
def hello():
    return "Hello from inside a container!"

@app.route("/init")
def init():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS visits (id SERIAL PRIMARY KEY, ts TIMESTAMP DEFAULT NOW());")
    cur.execute("INSERT INTO visits DEFAULT VALUES;")
    conn.commit()
    cur.execute("SELECT COUNT(*) FROM visits;")
    count = cur.fetchone()[0]
    cur.close()
    conn.close()
    return f"Visit logged. Total visits: {count} time"

if __name__ == "__main__":
    time.sleep(2)  # tiny wait for db to be ready on first boot
    app.run(host="0.0.0.0", port=5000)



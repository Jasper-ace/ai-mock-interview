import socket
import psycopg2
import sys

print("Python version:", sys.version)

host = "db.yvpulhwippdclrfbdouz.supabase.co"
print(f"Resolving {host}...")

try:
    ip = socket.gethostbyname(host)
    print(f"Resolved to: {ip}")
except Exception as e:
    print(f"DNS Resolution Failed: {e}")

print("Attempting to connect via psycopg2...")
try:
    conn = psycopg2.connect(
        "postgresql://postgres:Cq9gCrxK7NKsCcXh@db.yvpulhwippdclrfbdouz.supabase.co:5432/postgres",
        sslmode='require'
    )
    print("Connection successful!")
    conn.close()
except Exception as e:
    print(f"Connection Failed: {e}")

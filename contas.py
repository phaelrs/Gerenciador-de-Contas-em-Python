import sqlite3
from datetime import datetime, timedelta

def criar_banco():
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            valor REAL,
            vencimento TEXT
        )
    """)
    conn.commit()
    conn.close()


def adicionar_conta(nome, valor, vencimento):
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contas (nome, valor, vencimento) VALUES (?, ?, ?)",
                   (nome, valor, vencimento))
    conn.commit()
    conn.close()

def listar_contas():
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contas")
    contas = cursor.fetchall()
    conn.close()
    return contas

def contas_proximas():
    hoje = datetime.now().date()
    limite = hoje + timedelta(days=3)  
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contas WHERE vencimento <= ?", (str(limite),))
    contas = cursor.fetchall()
    conn.close()
    return contas

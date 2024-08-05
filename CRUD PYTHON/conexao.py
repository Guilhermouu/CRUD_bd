import sqlite3

def conectar():
    try:
        global banco, cursor
        banco = sqlite3.connect("cadastro.db")
        cursor = banco.cursor()
        print("Conexão sucedida!")
    except sqlite3.Error as erro:
        print("Falha na Conexão")
import sqlite3


def criar_clientes():
    conn = sqlite3.connect("c:/Python/Passagens_aerea/passagens_aereas/banco_dados.db")
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cpf INT (11),
            telefone VAR(14),
            data_nascimento date
        )
    ''')
    conn.commit()
    conn.close()
    

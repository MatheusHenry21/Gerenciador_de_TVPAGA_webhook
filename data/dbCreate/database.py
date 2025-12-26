import sqlite3

EXTERIOR = "dbCliente.db"

def resgatar():
    return sqlite3.connect(EXTERIOR)

def tabela_clientes_testes():
    db = resgatar()
    sql = db.cursor()

    sql.execute('''
        CREATE TABLE IF NOT EXISTS clientes_testes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            celular TEXT NOT NULL UNIQUE,
            plano DEFAULT '',
            data_inscricao DATE,
            data_vencimento DATE
        )
    ''')

    db.commit()
    db.close()

def tabela_clientes_efetivos():
    db = resgatar()
    sql = db.cursor()

    sql.execute('''
        CREATE TABLE IF NOT EXISTS clientes_efetivos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            celular TEXT NOT NULL UNIQUE,
            plano DEFAULT '',
            data_inscricao DATE,
            data_vencimento DATE
        )
    ''')

    db.commit()
    db.close()
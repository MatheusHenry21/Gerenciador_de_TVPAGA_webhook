
import sqlite3

SEQUENCIA = "status.db"

def create_table_sequent():
    return sqlite3.connect(SEQUENCIA)

def estado_conversa():
    db = create_table_sequent()
    sql = db.cursor()

    sql.execute('''
        CREATE TABLE IF NOT EXISTS status_conversa(
            telefone PRIMARY KEY,
            main TEXT DEFAULT NULL,
            submain TEXT DEFAULT NULL,
            submain2 TEXT DEFAULT NULL,
            nome TEXT DEFAULT NULL,
            celular INTEGER DEFAULT NULL,
            id INTEGER DEFAULT NULL
        )
    ''')
    db.commit()
    db.close()
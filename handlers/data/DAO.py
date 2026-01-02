
from handlers.data.table_sequencia import create_table_sequent as resgatar

def select_etapa(phone):
    db = resgatar()
    sql = db.cursor()
    sql.execute('''
        SELECT *
        FROM status_conversa
        WHERE telefone = ?;
    ''',(phone,)
    )
    data = sql.fetchone()
    db.close()
    return data

def update_main(phone, etapa):
    db = resgatar()
    sql = db.cursor()
    sql.execute('''
        UPDATE status_conversa
        SET main = ?
        WHERE telefone = ?;
    ''',(etapa, phone)
    )
    db.commit()
    db.close()

def update_submain(phone, etapa):
    db = resgatar()
    sql = db.cursor()
    sql.execute('''
        UPDATE status_conversa
        SET submain = ?
        WHERE telefone = ?;
    ''',(etapa, phone)
    )
    db.commit()
    db.close()

def update_submain2(phone, etapa):
    db = resgatar()
    sql = db.cursor()
    sql.execute('''
        UPDATE status_conversa
        SET submain2= ?
        WHERE telefone = ?;
    ''',(etapa, phone)
    )
    db.commit()
    db.close()

def update_name(phone, name):
    db = resgatar()
    sql = db.cursor()
    sql.execute('''
        UPDATE status_conversa
        SET nome = ?
        WHERE telefone = ?;
    ''',(name, phone)
    )
    db.commit()
    db.close()

def update_phone(phone, cll):
    db = resgatar()
    sql = db.cursor()
    sql.execute('''
        UPDATE status_conversa
        SET celular = ?
        WHERE telefone= ?;
    ''',(cll, phone)
    )
    db.commit()
    db.close()

def update_id(phone, id):
    db = resgatar()
    sql = db.cursor()
    sql.execute('''
        UPDATE status_conversa
        SET id = ?
        WHERE telefone = ?;
    ''',(id, phone)
    )
    db.commit()
    db.close()

def resetar_etapas_handler(phone):
    db = resgatar()
    sql = db.cursor()
    sql.execute('''
        UPDATE status_conversa
        SET main = NULL,
            submain = NULL,
            submain2 = NULL,
            nome = NULL,
            celular = NULL,
            id = NULL
        WHERE telefone = ?;
    ''',(phone,)
    )
    db.commit()
    db.close()

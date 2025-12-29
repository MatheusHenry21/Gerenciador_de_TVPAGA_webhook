
from webhook.handler.data_handler.table_sequencia import create_table_sequent as resgatar

db = resgatar()
sql = db.cursor()

def select_etapa(phone):
    sql.execute('''
        SELECT *
        FROM status_conversa
        WHERE telefone = ?
    ''',(phone,)
    )
    data = sql.fetchone()
    db.close()
    return data

def update_main(phone, etapa):
    sql.execute('''
        UPDATE status_conversa
        SET main = ?
        WHERE = ?
    ''',(etapa, phone)
    )
    db.commit()
    db.close()
def update_submain(phone, etapa):
    sql.execute('''
        UPDATE status_conversa
        SET submain = ?
        WHERE = ?
    ''',(phone, etapa)
    )

def update_submain2(phone, etapa):
    sql.execute('''
        UPDATE status_conversa
        SET submain2= ?
        WHERE = ?
    ''',(phone, etapa)
    )
    db.commit()
    db.close()

def update_name(phone, name):
    sql.execute('''
        UPDATE status_conversa
        SET nome = ?
        WHERE = ?
    ''',(phone, name)
    )
    db.commit()
    db.close()

def update_phone(phone, cll):
    sql.execute('''
        UPDATE status_conversa
        SET celular = ?
        WHERE = ?
    ''',(phone, cll)
    )
    db.commit()
    db.close()
from data.dbCreate.database import resgatar

def check_unique_celular(valor):
    db = resgatar()
    sql = db.cursor()

    sql.execute(
        '''
        SELECT CASE
            WHEN EXISTS(
                SELECT 1 FROM clientes_testes WHERE celular=?
                UNION
                SELECT 1 FROM clientes_efetivos WHERE celular=?
                )
                THEN 1
                ELSE 0
                END;        
        ''',(valor, valor)
    )
    
    dados = sql.fetchone()[0]
    db.close()

    return dados
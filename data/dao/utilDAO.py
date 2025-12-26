from data.dbCreate.database import resgatar

def existencia_nome_testes(nome):
    db = resgatar()
    sql = db.cursor()

    sql.execute('''
        SELECT CASE
            WHEN EXISTS(
                SELECT nome FROM clientes_testes WHERE nome=?
                )
                THEN 1
                ELSE 0
                END;
            ''', (nome,)) 
    
    dados = sql.fetchone()[0]
    db.close()
    return dados

def existencia_nome_efetivos(nome):
    db = resgatar()
    sql = db.cursor()

    sql.execute('''
        SELECT CASE
            WHEN EXISTS(
                SELECT nome FROM clientes_efetivos WHERE nome=?
                )
                THEN 1
                ELSE 0
                END;
            ''', (nome,)) 
    
    dados = sql.fetchone()[0]
    db.close()
    return dados

def existencia_celular_testes(numeroCll):
    db = resgatar()
    sql = db.cursor()

    sql.execute('''
        SELECT CASE
            WHEN EXISTS(
                SELECT 1 FROM clientes_testes WHERE celular=?
                )
                THEN 1
                ELSE 0
            END;
        ''', (numeroCll,)      
            )
    dados = sql.fetchone()[0]
    db.close()

    return dados

def existencia_celular_efetivos(numeroCll):
    db = resgatar()
    sql = db.cursor()

    sql.execute('''
        SELECT CASE
            WHEN EXISTS(
                SELECT 1 FROM clientes_efetivos WHERE celular=?
                )
                THEN 1
                ELSE 0
            END;
        ''',(numeroCll,)
        )
    
    dados = sql.fetchone()[0]
    db.close()

    return dados

def existencia_id_teste(id):
    db = resgatar()
    sql = db.cursor()

    sql.execute('''
        SELECT CASE
            WHEN EXISTS(
                SELECT 1 FROM clientes_testes WHERE id=?
                )
                THEN 1
                ELSE 0
                END;'''
                ,(id, )       
        )
    
    dados = sql.fetchone()[0]
    db.close()
    return dados

def existencia_id_efetivos(id):
    db = resgatar()
    sql = db.cursor()

    sql.execute('''
        SELECT CASE
            WHEN EXISTS(
                SELECT 1 FROM clientes_efetivos WHERE id=?
                )
                THEN 1
                ELSE 0
                END;'''
                ,(id, )       
        )
    
    dados = sql.fetchone()[0]
    db.close()
    return dados

def excluir_bancos_efetivos_testes():
    db = resgatar()
    sql = db.cursor()
    sql.execute('''
        DELETE FROM clientes_efetivos
        ''')
    sql.execute('''
        DELETE FROM clientes_testes
        ''')
    db.commit()
    db.close()

def existencia_ambos_clientes():
    db = resgatar()
    sql = db.cursor()

    sql.execute('''
        SELECT CASE
            WHEN EXISTS(
                SELECT * FROM clientes_efetivos
                UNION 
                SELECT * FROM clientes_testes
                )
                THEN 1
                ELSE 0
                END;
        ''')
    
    dados = sql.fetchone()[0]
    db.close()
    return dados
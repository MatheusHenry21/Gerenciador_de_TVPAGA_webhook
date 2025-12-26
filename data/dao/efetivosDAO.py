
from data.dbCreate.database import resgatar

def add_efetivos(nome, celular, cadastro, vencimento):
    db = resgatar()
    sql = db.cursor()

    sql.execute(
        '''INSERT INTO clientes_efetivos(nome, celular, plano, data_inscricao, data_vencimento)
            VALUES (?, ?, "EFETIVO", ?, ?);''',
            (nome, celular, cadastro, vencimento)
        )
    
    db.commit()
    db.close()

def listar_efetivos():
    db = resgatar()
    sql = db.cursor()

    sql.execute(
        '''SELECT * FROM clientes_efetivos;'''
    )
    dados = sql.fetchall()

    db.close()
    return dados

def remover_efetivos(id):
    db = resgatar()
    sql = db.cursor()

    sql.execute(
        '''DELETE FROM clientes_efetivos WHERE id=?;''',
        (id,)
    )

    db.commit()
    db.close()

def buscar_cliente_efetivo_celular(celular):
    db = resgatar()
    sql = db.cursor()

    sql.execute(
        '''SELECT * FROM clientes_efetivos WHERE celular=?;''',
        (celular,)
    )
    dados = sql.fetchall()

    db.close()
    return dados

def buscar_cliente_efetivo_id(id):
    db = resgatar()
    sql = db.cursor()

    sql.execute(
        '''SELECT * FROM clientes_efetivos WHERE id=?;''',
        (id,)
    )
    dados = sql.fetchall()

    db.close()
    return dados

def buscar_cliente_efetivo_nome(nome):
    db = resgatar()
    sql = db.cursor()

    sql.execute(
        '''SELECT * FROM clientes_efetivos WHERE nome=?;''',
        (nome,)
    )
    dados = sql.fetchall()

    db.close()
    return dados

def atualizar_nome_cliente_efetivo(nome, id):
    db = resgatar()
    sql = db.cursor()

    sql.execute('''
        UPDATE clientes_efetivos
        SET nome=?
        WHERE id=?
        ''',(nome, id))
    
    db.commit()
    db.close()

def atualizar_celular_cliente_efetivo(celular, id):
    db = resgatar()
    sql = db.cursor()

    sql.execute('''
        UPDATE clientes_efetivos
        SET celular=?
        WHERE id=?
        ''',(celular, id))
    
    db.commit()
    db.close()

def quantidade_clientes_efetivos():
    db = resgatar()
    sql = db.cursor()

    sql.execute(
        '''SELECT COUNT(*) FROM clientes_efetivos;'''
    )

    quantidade = sql.fetchone()[0]
    db.close()
    return quantidade

def resgatar_data_vencimento_efetivos(id):
    db = resgatar()
    sql = db.cursor()

    sql.execute(
        '''SELECT data_vencimento FROM clientes_efetivos WHERE id=?;
        ''', (id,)
    )

    data = sql.fetchone()
    db.commit()
    return data

def clientes_vencendo():
    db = resgatar()
    sql = db.cursor()

    sql.execute("""
        SELECT id, nome, celular, (julianday(data_vencimento) - julianday('now')) AS dias
        FROM clientes_efetivos
        WHERE 
            (julianday(data_vencimento) - julianday('now')) <= 5
            AND (julianday(data_vencimento) - julianday('now')) >= 0
        ORDER BY dias ASC;
    """)

    clientes = sql.fetchall()
    db.close()
    return clientes

def clientes_vencidos_efetivos():
    db = resgatar()
    sql = db.cursor()

    sql.execute("""
        SELECT id, nome, celular, (julianday(data_vencimento) - julianday('now')) AS dias
        FROM clientes_efetivos
        WHERE 
            (julianday(data_vencimento) - julianday('now')) < 0
        ORDER BY dias ASC;
    """)

    clientes = sql.fetchall()
    db.close()
    return clientes

def renovar_assinatura_resgatar(id):
    db = resgatar()
    sql = db.cursor()

    sql.execute(
        '''
        SELECT data_vencimento FROM clientes_efetivos
        WHERE id=?
        ;''',(id, )
    )

    dataVencimento = sql.fetchone()[0]
    db.close()
    return dataVencimento

def renovar_assinatura_salvar(novaData, id):
    db = resgatar()
    sql = db.cursor()

    sql.execute(
        '''
        UPDATE clientes_efetivos
        SET data_vencimento=?
        WHERE id=?
        ;''',(novaData, id)
    )
    db.commit()
    db.close()
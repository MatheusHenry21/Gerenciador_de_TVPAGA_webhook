
from data.dbCreate.database import resgatar

def add_testes(nome, celular, inscricao, fimTeste):
    db = resgatar()
    sql = db.cursor()

    sql.execute(
        '''INSERT INTO clientes_testes(nome, celular, plano, data_inscricao, data_vencimento)
            VALUES (?, ?, "PLANO DE TESTE", ?, ?)''',
            (nome, celular, inscricao, fimTeste)
        )
    
    db.commit()
    db.close()

def listar_testes():
    db = resgatar()
    sql = db.cursor()

    sql.execute(
        '''SELECT * FROM clientes_testes'''
    )
    dados = sql.fetchall()

    db.close()
    return dados

def remover_testes(id):
    db = resgatar()
    sql = db.cursor()

    sql.execute(
        '''DELETE FROM clientes_testes WHERE id=?''',
        (id,)
    )
    db.commit()

    db.close()

def buscar_cliente_teste_celular(celular):
    db = resgatar()
    sql = db.cursor()

    sql.execute(
        '''SELECT * FROM clientes_testes WHERE celular=?;''',
        (celular,)
    )
    dados = sql.fetchall()

    db.close()
    return dados

def buscar_cliente_teste_id(id):
    db = resgatar()
    sql = db.cursor()

    sql.execute(
        '''SELECT * FROM clientes_testes WHERE id=?;''',
        (id,)
    )
    dados = sql.fetchall()

    db.close()
    return dados

def buscar_cliente_teste_nome(nome):
    db = resgatar()
    sql = db.cursor()

    sql.execute(
        '''SELECT * FROM clientes_testes WHERE nome=?;''',
        (nome,)
    )
    dados = sql.fetchall()

    db.close()
    return dados

def atualizar_nome_cliente_teste(nome, id):
    db = resgatar()
    sql = db.cursor()

    sql.execute('''
        UPDATE clientes_testes
        SET nome=?
        WHERE id=?
        ''',(nome, id))
    
    db.commit()
    db.close()

def atualizar_celular_cliente_teste(celular, id):
    db = resgatar()
    sql = db.cursor()

    sql.execute('''
        UPDATE clientes_testes
        SET celular=?
        WHERE id=?
        ''',(celular, id))
    
    db.commit()
    db.close()

def quantidade_clientes_testes():
    db = resgatar()
    sql = db.cursor()

    sql.execute(
        '''
        SELECT COUNT(*) FROM clientes_testes;
        '''
    )

    quantidade = sql.fetchone()[0]
    db.close()
    return quantidade

def clientes_vencidos_teste():
    db = resgatar()
    sql = db.cursor()

    sql.execute("""
        SELECT id, nome, celular, (julianday(data_vencimento) - julianday('now')) AS dias
        FROM clientes_testes
        WHERE 
            (julianday(data_vencimento) - julianday('now')) < 0
        ORDER BY dias ASC;
    """)

    clientes = sql.fetchall()
    db.close()
    return clientes
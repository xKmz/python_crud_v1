# -*- coding: UTF-8 -*-

import psycopg2

# criar a tabela básica do projeto! :)
# basta inserir os dados de seu PostgreSQL na variável conn

try:
    conn = psycopg2.connect(user = "PREENCHER",
                            password = "PREENCHER",
                            host = "PREENCHER",
                            port = "PREENCHER",
                            database = "PREENCHER")
    print 'Conectando...'
    print '...'
    criar_tabela = "CREATE TABLE clientes (id serial primary key, nome varchar(255), idade decimal, email varchar(255));"
    conn.cursor().execute(criar_tabela)
    print 'Criando tabela...'
    print '...'
    conn.commit()
    print ' '
    print 'Sucesso! :D'
        
except (Exception, psycopg2.DatabaseError) as error:
    print(error)

finally:
    if conn is not None:
        conn.close()
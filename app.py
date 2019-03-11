# -*- coding: UTF-8 -*-

import psycopg2

conn = psycopg2.connect(user = "postgres",
                                password = "master",
                                host = "localhost",
                                port = "5432",
                                database = "teste")
cursor = conn.cursor()

def cadastro():
        print ' '
        print '##################################################################'
        print '#                        Digite o Nome:                          #'
        print '##################################################################'
        print ' '
        nome = raw_input()
        print ' '
        print '##################################################################'
        print '#                        Digite a Idade:                         #'
        print '##################################################################'
        print ' '
        idade = raw_input()
        print ' '
        print '##################################################################'
        print '#                        Digite o Email:                         #'
        print '##################################################################'
        print ' '
        email = raw_input()

        try:
            cursor.execute("INSERT INTO clientes (nome, idade, email) VALUES ('%s', '%s', '%s')" % (nome, idade, email))
            conn.commit()
            print ' '
            print ('Os dados de %s foram adicionados com sucesso!') % (nome)

        except:
            print ' '
            print "Falha ao acessar o banco de dados."
            print "Verifique as configurações de acesso."
            print ' '
        
def lista():
        print ' '
        print '##################################################################'
        print '#                           Clientes:                            #'
        print '##################################################################'
        print ' '

        try:
            cursor.execute('SELECT * FROM clientes')
            for cliente in cursor.fetchall():
                print 'Nome: %s, Idade: %s, Email: %s' % (cliente[1], cliente[2], cliente[3])
        
        except:
            print ' '
            print "Falha ao acessar o banco de dados."
            print "Verifique as configurações de acesso."
            print ' '

def remove():
    print ' '
    print '##################################################################'
    print '#          Digite o nome que você gostaria de remover:           #'
    print '##################################################################'
    print ' '
    nome = raw_input()

    try:
        sql_select_query = "SELECT * FROM clientes WHERE nome = %s"
        cursor.execute(sql_select_query, (nome, ))
        cliente = cursor.fetchone()
        
        if (nome in cliente):
            try:
                sql_delete_query = "DELETE FROM clientes WHERE nome = %s"
                cursor.execute(sql_delete_query, (nome,))
                conn.commit()
                print ' '
                print ('Os dados de %s foram removidos com sucesso!') % (nome)
                print ' '

            except:
                    print ' '
                    print "Falha ao acessar o banco de dados."
                    print "Verifique as configurações de acesso."
                    print ' '

    except (Exception, psycopg2.Error) as error:
        print ' '
        print("Poxa! O nome não existe. Tente novamente :(")
        print ' '

def alterar():
    print ''
    print 'Digite o nome do cadastro que você gostaria de alterar?'
    print ''
    nome = raw_input()
    print ''

    try:
        sql_select_query = "SELECT * FROM clientes WHERE nome = %s"
        cursor.execute(sql_select_query, (nome, ))
        cliente = cursor.fetchone()
        
        if (nome in cliente):
            escolha = ''
            while(escolha != '0'):
                print ' '
                print '##################################################################'
                print '#                                                                #'
                print '#        Qual das opções você gostaria de atualizar?             #'
                print '#                                                                #'
                print '#        1) Nome 2) Idade 3) Email 0) Voltar ao Menu             #'
                print '#                                                                #'
                print '##################################################################'
                print ' '
                escolha = raw_input()
                print ' '

                if(escolha == '1'):
                    print ' '
                    print 'Digite o novo nome:'
                    print ' '
                    novo_nome = raw_input()
                    
                    try:
                        sql_update_query = "UPDATE clientes SET nome = %s WHERE id = %s"
                        cursor.execute(sql_update_query, (novo_nome, cliente[0]))
                        conn.commit()
                    
                    except:
                        print ' '
                        print "Falha ao acessar o banco de dados."
                        print "Verifique as configurações de acesso."
                        print ' '

                elif(escolha == '2'):
                    print ' '
                    print 'Digite a nova idade:'
                    print ' '
                    nova_idade = raw_input()
                    
                    try:
                        sql_update_query = "UPDATE clientes SET idade = %s WHERE id = %s"
                        cursor.execute(sql_update_query, (nova_idade, cliente[0]))
                        conn.commit()
                    
                    except:
                        print ' '
                        print "Falha ao acessar o banco de dados."
                        print "Verifique as configurações de acesso."
                        print ' '

                elif(escolha == '3'):
                    print ' '
                    print 'Digite o novo email:'
                    print ' '
                    novo_email = raw_input()
                    
                    try:
                        sql_update_query = "UPDATE clientes SET email = %s WHERE id = %s"
                        cursor.execute(sql_update_query, (novo_email, cliente[0]))
                        conn.commit()

                    except:
                        print ' '
                        print "Falha ao acessar o banco de dados."
                        print "Verifique as configurações de acesso."
                        print ' '

    except (Exception, psycopg2.Error) as error:
        print ' '
        print("Poxa! O nome não existe :(")
        print ' '

def procurar():
    print ' '
    print 'Quem você gostaria de procurar?'
    print ' '
    nome_a_procurar = raw_input()

    try:
        sql_select_query = "SELECT * FROM clientes WHERE nome = %s"
        cursor.execute(sql_select_query, (nome_a_procurar, ))
        resultado = cursor.fetchone()
        print ' '
        print 'O nome %s esta na lista!' % (nome_a_procurar)
        print ' '

    except (Exception, psycopg2.Error) as error:
        print ' '
        print("O nome não existe. Procure por outro nome :D")
        print ' '

def menu():
    escolha = ''
    print ' '
    print 'Bem-vindo ao cadastro feliz! :D'
    print ' '
    while(escolha != '0'):
        print ' '
        print '##################################################################'
        print '#                                                                #'
        print '#                     Escolha uma opção:                         #'
        print '#               1) Cadastrar 2) Listar 3) Remover                #'
        print '#                4) Alterar 5) Procurar 0) Sair                  #'
        print '#                                                                #'
        print '##################################################################'
        print ' '
        escolha = raw_input()
        print ' '
        
        if(escolha == '0'):
            quit()

        elif(escolha == '1'):
            cadastro()

        elif(escolha == '2'):
            lista()

        elif(escolha == '3'):
            remove()
            
        elif(escolha == '4'):
            alterar()
        
        elif(escolha == '5'):
            procurar()

        else:
            print 'Opção inválida!'

menu()
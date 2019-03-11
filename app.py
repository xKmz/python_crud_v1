# -*- coding: UTF-8 -*-

import psycopg2

def conecta_banco():
    conexao = ''
    try:
        conexao = psycopg2.connect(user = "CONFIGURAR",
                                password = "CONFIGURAR",
                                host = "CONFIGURAR",
                                port = "CONFIGURAR",
                                database = "CONFIGURAR")
    except:
        print "Ops!!"
        erro_de_conexao()
   
    return conexao

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
            conexao = conecta_banco()
            cursor = conexao.cursor()
            cursor.execute("INSERT INTO clientes (nome, idade, email) VALUES ('%s', '%s', '%s')" % (nome, idade, email))
            conexao.commit()
            print ' '
            print ('Os dados de %s foram adicionados com sucesso!') % (nome)

        except:
            erro_de_conexao()
        
        finally:
            conexao.close()

def lista():
        print ' '
        print '##################################################################'
        print '#                           Clientes:                            #'
        print '##################################################################'
        print ' '

        try:
            conexao = conecta_banco()
            cursor = conexao.cursor()
            cursor.execute('SELECT * FROM clientes')
            for cliente in cursor.fetchall():
                print 'Nome: %s, Idade: %s, Email: %s' % (cliente[1], cliente[2], cliente[3])
        
        except:
            erro_de_conexao()

        finally:
            conexao.close()

def remove():
    print ' '
    print '##################################################################'
    print '#          Digite o nome que você gostaria de remover:           #'
    print '##################################################################'
    print ' '
    nome = raw_input()

    try:
        conexao = conecta_banco()
        cursor = conexao.cursor()
        sql_select_query = "SELECT * FROM clientes WHERE nome = %s"
        cursor.execute(sql_select_query, (nome, ))
        cliente = cursor.fetchone()
        
        if (nome in cliente):
            try:
                sql_delete_query = "DELETE FROM clientes WHERE nome = %s"
                cursor.execute(sql_delete_query, (nome,))
                conexao.commit()
                print ' '
                print ('Os dados de %s foram removidos com sucesso!') % (nome)
                print ' '

            except:
                erro_de_conexao()

            finally:
                conexao.close()

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
        conexao = conecta_banco()
        cursor = conexao.cursor()
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
                        conexao.commit()
                    
                    except:
                        erro_de_conexao()

                elif(escolha == '2'):
                    print ' '
                    print 'Digite a nova idade:'
                    print ' '
                    nova_idade = raw_input()
                    
                    try:
                        sql_update_query = "UPDATE clientes SET idade = %s WHERE id = %s"
                        cursor.execute(sql_update_query, (nova_idade, cliente[0]))
                        conexao.commit()
                    
                    except:
                        erro_de_conexao()

                elif(escolha == '3'):
                    print ' '
                    print 'Digite o novo email:'
                    print ' '
                    novo_email = raw_input()
                    
                    try:
                        sql_update_query = "UPDATE clientes SET email = %s WHERE id = %s"
                        cursor.execute(sql_update_query, (novo_email, cliente[0]))
                        conexao.commit()

                    except:
                        erro_de_conexao()

    except (Exception, psycopg2.Error) as error:
        print ' '
        print("Poxa! O nome não existe :(")
        print ' '

    finally:
        conexao.close()

def procurar():
    print ' '
    print 'Quem você gostaria de procurar?'
    print ' '
    nome_a_procurar = raw_input()

    try:
        conexao = conecta_banco()
        cursor = conexao.cursor()
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
    
    finally:
        conexao.close()

def exportar():
    try:
        conexao = conecta_banco()
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM clientes')
        arquivo_export = open('clientes.csv','a')
        for cliente in cursor.fetchall():
            arquivo_export.write(" " + cliente[1] + ", " + str(cliente[2]) + ", " + cliente[3] + " \n")
        arquivo_export.close()
        print 'Clientes exportados com sucesso! :P'
        print 'A tabela clientes.csv encontra-se no local de seu sistema!'
        print ' '

    except:
        erro_de_conexao()

    finally:
        conexao.close()

def erro_de_conexao():
    print ' '
    print "Falha ao acessar o banco de dados."
    print "Verifique as configurações de acesso."
    print ' '

def menu():
    escolha = ''
    print ' '
    print '##################################################################'
    print '#                                                                #'
    print '#                Bem-vindo ao cadastro feliz! :D                 #'
    print '#                                                                #'
    print '#           Esperamos que você goste de nosso sistema!           #'
    print '#                 Dúvidas e sugestões no github                  #'
    print '#                                                                #'
    print '##################################################################'
    print ' '
    
    while(escolha != '0'):
        print ' '
        print '##################################################################'
        print '#                                                                #'
        print '#                     Escolha uma opção:                         #'
        print '#               1) Cadastrar 2) Listar 3) Remover                #'
        print '#           4) Alterar 5) Procurar 6) Exportar Clientes          #'
        print '#                           0) Sair                              #'
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
        
        elif(escolha == '6'):
            exportar()

        else:
            print 'Opção inválida!'

menu()
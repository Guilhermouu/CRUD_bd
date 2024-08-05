import sqlite3
import conexao

#Criando uma função para coletar dados do cliente
def cadastrarCliente():
    try:
        conexao.conectar()
        nome = input("Informe o seu nome: ")
        sobrenome = input("Informe o seu sobrenome: ")
        idade = int(input("Informe a sua idade: "))
        cpf = int(input("Informe o seu CPF: "))
        telefone = str(input("Informe o seu N de telefone: "))
        endereco = input("Informe o seu endereço: ")
        cidade = input("Informe a cidade: ")
        estado = input("Informe o estado: ")

        inserir_cliente = "INSERT INTO  cliente VALUES ('"+nome+"','"+sobrenome+"','"+str(idade)+"','"+str(cpf)+"','"+str(telefone)+"','"+endereco+"','"+cidade+"','"+estado+"')"
        conexao.cursor.execute(inserir_cliente)
        conexao.banco.commit()
        conexao.banco.close()
        print("CLIENTE CADASTRADO COM SUCESSO")
    except sqlite3.Error as erro:
        print("Erro ao cadastrar Cliente", erro)
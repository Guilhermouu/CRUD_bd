import sqlite3
import conexao 

def exibirCliente():
    conexao.conectar()
    resultado = conexao.cursor.execute("SELECT * FROM cliente").fetchall()
    for result in resultado:
        print("######################")
        print("Nome: ",result[0])
        print("Sobrenome: ",result[1])
        print("Idade: ",result[2])
        print("CPF: ",result[3])
        print("Telefone: ",result[4])
        print("Endereco: ",result[5])
        print("Cidade: ",result[6])
        print("Estado: ",result[7])
    #conexao.banco.close()

def consultarCliente():
    conexao.conectar()
    cpf = input("Informe o CPF que deseja consultar: ")
    try:
        resultado = conexao.banco.execute('''SELECT * FROM cliente where cpf = ?''',(cpf,)).fetchall()
        if(resultado == []):
            print("CPF não encontrado!")
        else:
            for result in resultado:
                print("######################")
                print("Nome: ",result[0])
                print("Sobrenome: ",result[1])
                print("Idade: ",result[2])
                print("CPF: ",result[3])
                print("Telefone: ",result[4])
                print("Endereco: ",result[5])
                print("Cidade: ",result[6])
                print("Estado: ",result[7])
        return cpf
        #print("cliente encontrado ",resultado)
    except sqlite3.Error as erro:
        print("Erro ao encontrar Cliente",erro)
    #conexao.banco.close()

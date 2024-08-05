import sqlite3
from funcaMenu  import menu
import conexao 
import criarTable
import insertCliente
import selectCliente
import update
import deletar
#Criação da tabela Cliente
criarTable.criar()

opcao = menu()
while (opcao !='6'):

    if(opcao == '1'):
        insertCliente.cadastrarCliente()
    elif(opcao == '2'):
        selectCliente.exibirCliente()
    elif(opcao == '3'):
        selectCliente.consultarCliente()
    elif(opcao == '4'):
        update.alterarDados()
    elif(opcao == '5'):
        deletar.delet()
    opcao = menu()

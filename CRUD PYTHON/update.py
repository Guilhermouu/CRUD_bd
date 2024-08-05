import conexao
import selectCliente
 
 
def alterarDados():
    conexao.conectar()
    print("######### Alteração de dados ########")
    global cpfPesquisar
    cpfPesquisar = selectCliente.consultarCliente()
    if(cpfPesquisar != []):
        dado_update = input("O que deseja alterar\nNome\nSobrenome\nIdade\nCPF\nTelefone\nEndereco\nCidade\nEstado\n ").lower()
        atualizacao(dado_update)
 
def atualizacao(dado_update):
    if dado_update == 'nome':
        novo_nome = input("Novo Nome: ")
        conexao.cursor.execute("UPDATE cliente SET nome = '"+novo_nome+"'WHERE cpf = ?",(cpfPesquisar,))
        print("Nome alterado com sucesso !!")
        
    elif dado_update == 'sobrenome':
        novo_sobrenome = input("Novo Sobrenome: ")
        conexao.cursor.execute("UPDATE cliente SET sobrenome = '"+novo_sobrenome+"'WHERE cpf = ?",(cpfPesquisar,))
        print("Nome alterado com sucesso !!")
    elif dado_update == 'idade':
        novo_idade = input("Nova Idade: ")
        conexao.cursor.execute("UPDATE cliente SET idade = '"+novo_idade+"'WHERE cpf = ?",(cpfPesquisar,))
        print("Nome alterado com sucesso !!")
                                                                                                                                                  
    elif dado_update == 'cpf':
        novo_cpf = input("Novo CPF:")
        conexao.cursor.execute("UPDATE cliente SET cpf = '"+novo_cpf+"'WHERE cpf = ?",(cpfPesquisar,))
        print("Nome alterado com sucesso !!")

    elif dado_update == 'estado':
        novo_estado = input("Novo Estado: ")
        conexao.cursor.execute("UPDATE cliente SET estado = '"+novo_estado+"'WHERE cpf = ?",(cpfPesquisar,))

    elif dado_update == 'telefone':
        novo_telefone = input("Novo Telefone: ")
        conexao.cursor.execute("UPDATE cliente SET telefone = '"+novo_telefone+"'WHERE cpf = ?",(cpfPesquisar,))
        print("Nome alterado com sucesso !!")

    elif dado_update == 'endereco':
        novo_enderco = input("Novo Endereco: ")                 
        conexao.cursor.execute("UPDATE cliente SET endereco = '"+novo_enderco+"'WHERE cpf = ?",(cpfPesquisar,))
        print("Nome alterado com sucesso !!")

    elif dado_update == 'cidade':
        novo_cidade = input("Novo Cidade: ")
        conexao.cursor.execute("UPDATE cliente SET cidade = '"+novo_cidade+"'WHERE cpf = ?",(cpfPesquisar,))
        print("Nome alterado com sucesso !!")

    elif dado_update == 'estado':
        novo_estado = input("Novo Estado: ")
        conexao.cursor.execute("UPDATE cliente SET       estado = '"+novo_estado+"'WHERE cpf = ?",(cpfPesquisar,))
        print("Nome alterado com sucesso !!")

    else:
        print("Nome não alterado")
    conexao.banco.commit()
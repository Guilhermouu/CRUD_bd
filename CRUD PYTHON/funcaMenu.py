def menu():
    print(">>>>>>>>>>< Menu Cadastrais ><<<<<<<<<<")
    print("O que deseja fazer:")
    print(""" 1 - Cadastrar Clientes:
          \n 2 - Exinbir Clientes:
          \n 3 - Consultar Cliente pelo CPF:
          \n 4 - Alterar Dados Cadastrais:
          \n 5 - Excluir Cliente:
          \n 6 - Sair""")
    print(">>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<")
    global opcao
    opcao = input()
    return opcao
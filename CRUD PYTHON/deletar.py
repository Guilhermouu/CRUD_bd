import sqlite3
import conexao
def delet():
    conexao.conectar()
    cpf=input("Informe o CPF que deseja deletar:")
    try:
        resultado= conexao.banco.execute('''SELECT *FROM cliente where cpf =? ''',(cpf,)).fetchall()
        if(resultado == []):
            print('CPF não foi encontrado!')
        else:
            banco=sqlite3.connect('cadastro.db')

            cursor= banco.cursor()

            cursor.execute("DELETE FROM cliente WHERE cpf= '"+cpf+"'")

            banco.commit()
            banco.close
            print('Dado Excluido com Sucesso')

    except Exception as erro:
            print('Erro ao excluir dados: ', erro)
        

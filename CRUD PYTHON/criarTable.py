import conexao


conexao.conectar()
def criar():
    criar_table = "CREATE TABLE IF NOT EXISTS cliente(nome string, sobrenome string, idade integer, cpf integer, telefone integer, endereco string, cidade string, estado string)"
    conexao.cursor.execute(criar_table)
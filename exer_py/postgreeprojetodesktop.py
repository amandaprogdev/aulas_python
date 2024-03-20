import psycopg2
conexao = psycopg2.connect(
host = "localhost",
user = "postgres",
password = "0000",
database = "postgres"
)
# Menu principal do sistema desktop
def menu():
    while True:
        print("1.Cadastrar Aluno")
        opcao = input('Digite a opção desejada: ')
        if opcao == ("1"):
            print("Cadastrar Aluno")
        else:
            print("Opção Inválida. Tente Novamente")
        
    # Chamar a função do menu principal: menu()
    
    # Fun
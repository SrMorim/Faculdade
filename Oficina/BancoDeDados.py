import mysql.connector

#Conexão com o banco de dados
def conectar():
    nome = input("Digite o login: ")
    email = input("Digite a email: ")
    senha = input("Digite a senha: ")
    
    abacate = mysql.connector.connect(
    host='localhost', 
    user="root",
    password="")
    print("Conexão realizada com sucesso", abacate)
    
    cursor = abacate.cursor()
    cursor.execute(f"insert into oficina.usuarios (nome, email, senha) values ('{nome}', '{email}', '{senha}')")

    abacate.commit()


#Inserir  dados no banco de dados
conectar()

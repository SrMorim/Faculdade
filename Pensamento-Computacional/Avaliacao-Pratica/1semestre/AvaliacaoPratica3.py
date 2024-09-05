#Imports
import os
def Avaliacao_Pratica_3A():
    # Inicializar variáveis
    count = 0
    sum_values = 0
    count_greater_than_20 = 0

    # Ler valores do usuário
    while True:
        value = input("Digite um valor real (ou 'q' para encerrar e mostrar o resultado): ")
        if value == 'q':
            break

        # Converter entrada para float
        value = float(value)

        # Atualizar variáveis
        count += 1
        sum_values += value

        if value > 20:
            count_greater_than_20 += 1

    # Calcular média
    average = sum_values / count if count != 0 else 0

    # Exibir resultados
    print("Quantidade de valores digitados:", count)
    print("Soma dos valores digitados:", sum_values)
    print("Média aritmética dos valores digitados:", average)
    print("Quantidade de valores maiores que 20:", count_greater_than_20)

def Avaliacao_Pratica_3B():
    # Inicializar variáveis
    count_students = 0
    count_passed = 0
    count_failed = 0

    # Ler notas dos alunos
    while True:
        grade = input("Digite a nota do aluno (ou 'q' para encerrar e mostrar o resultado): ")
        if grade == 'q':
            break

        # Converter entrada para float
        grade = float(grade)

        # Atualizar variáveis
        count_students += 1
        if grade >= 5:
            count_passed += 1
        else:
            count_failed += 1

    # Exibir resultados
    print("Quantidade de alunos que fizeram a prova:", count_students)
    print("Quantidade de alunos aprovados:", count_passed)
    print("Quantidade de alunos reprovados:", count_failed)

def Avaliacao_Pratica_3C():
    # Inicializar variáveis
    sum_even = 0
    count_even = 0
    sum_odd = 0
    count_odd = 0

    # Ler valores do usuário
    while True:
        value = int(input("Digite um valor inteiro (ou 0 para encerrar e mostrar o resultado): "))
        if value == 0:
            break

        # Atualizar variáveis
        if value % 2 == 0:
            sum_even += value
            count_even += 1
        else:
            sum_odd += value
            count_odd += 1

    # Calcular médias
    average_even = sum_even / count_even if count_even != 0 else 0
    average_odd = sum_odd / count_odd if count_odd != 0 else 0

    # Exibir resultados
    print("Média aritmética dos números pares:", average_even)
    print("Média aritmética dos números ímpares:", average_odd)
#Menu
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Avaliação\nEscolha\n[a]Questão A\n[b]Questão B\n[c]Questão C\n[e]Exit')

    escolha = str(input('>>> '))
    if escolha == 'a':
        Avaliacao_Pratica_3A()
        break
    elif escolha == 'b':
        Avaliacao_Pratica_3B()
        break
    elif escolha == 'c':
        Avaliacao_Pratica_3C()
        break
    elif escolha == 'e':
        print('bye bye')
        break
    else:
        input('escolha entre a, b, c ou d.')
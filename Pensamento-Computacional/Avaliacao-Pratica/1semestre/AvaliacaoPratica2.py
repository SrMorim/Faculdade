import os

def Avaliacao_Pratica_2A():
    valor1 = float(input("Insira o primeiro valor: "))
    valor2 = float(input("Insira o segundo valor: "))
    valor3 = float(input("Insira o terceiro valor: "))
    valormax = max(valor1, valor2, valor3)
    print("O maior valor é:", valormax)

def Avaliacao_Pratica_2B():
    valor1 = float(input("Insira o primeiro valor: "))
    valor2 = float(input("Insira o segundo valor: "))
    valor3 = float(input("Insira o terceiro valor: "))

    if valor1 >= valor2 and valor1 >= valor3:
        valormax = valor1
    elif valor2 >= valor1 and valor2 >= valor3:
        valormax = valor2
    else:
        valormax = valor3
    print("O maior valor é:", valormax)

def Avaliacao_Pratica_2C():
    print('''
░█▀▀░█▀█░█░░░█▀▀░█░█░█░░░█▀█░█▀▄░█▀█░█▀▄░█▀█
░█░░░█▀█░█░░░█░░░█░█░█░░░█▀█░█░█░█░█░█▀▄░█▀█
░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀▀░░▀▀▀░▀░▀░▀░▀
''')
    print('Menu:\n[1]Somar\n[2]Subtrair\n[3]Multiplicar\n[4]Dividir\n[5]Sair')
    escolha = int(input('Escolha: '))

    if escolha == 1:
        n1 = float(input('Insira o primeiro valor: '))
        n2 = float(input('Insira o segundo valor: '))
        print('Resultado:', n1 + n2)
    elif escolha == 2:
        n1 = float(input('Insira o primeiro valor: '))
        n2 = float(input('Insira o segundo valor: '))
        print('Resultado:', n1 - n2)
    elif escolha == 3:
        n1 = float(input('Insira o primeiro valor: '))
        n2 = float(input('Insira o segundo valor: '))
        print('Resultado:', n1 * n2)
    elif escolha == 4:
        n1 = float(input('Insira o primeiro valor: '))
        n2 = float(input('Insira o segundo valor: '))
        print('Resultado:', n1 / n2)
    elif escolha == 5:
        print('bye bye')

#main
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Avaliação\nEscolha\n[a]Questão A\n[b]Questão B\n[c]Questão C\n[e]Exit')

    escolha = str(input('>>> '))
    if escolha == 'a':
        Avaliacao_Pratica_2A()
        break
    elif escolha == 'b':
        Avaliacao_Pratica_2B()
        break
    elif escolha == 'c':
        Avaliacao_Pratica_2C()
        break
    elif escolha == 'e':
        print('bye bye')
        break
    else:
        input('escolha entre a, b, c ou d.')

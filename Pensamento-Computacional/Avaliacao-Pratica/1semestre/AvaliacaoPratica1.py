#Avaliação feita no VSCode
#Lib usada
import math
import os

#Calculos
def Avaliacao_Pratica_1A():
#A) Implemente o programa que calcule o volume de uma esfera de raio R. O usuário fornecerá o dado necessário.
    
    raio = float(input('Digite o raio R : '))
    volume = (4/3) * 3.14 * (raio**2)

    input(f"O volume da efera de raio R {raio} é igual à: {volume:.2f}")

def Avaliacao_Pratica_1B():
#B) Construa o programa que tendo como dados de entrada dois pontos quaisquer do plano cartesiano, P(x1, y1) e Q(x2, y2), calcule a distância entre eles.
    def calcular_distancia(x1, y1, x2, y2):
        distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        return distancia

    x1 = float(input("Digite a coordenada x1 de P: "))
    y1 = float(input("Digite a coordenada y1 de P: "))
    x2 = float(input("Digite a coordenada x2 de Q: "))
    y2 = float(input("Digite a coordenada y2 de Q: "))

    distancia = calcular_distancia(x1, y1, x2, y2)

    input(f"A distância entre os pontos P({x1}, {y1}) e Q({x2}, {y2}) é {distancia:.2f}")

def Avaliacao_Pratica_1C(): 
# C) Desenvolva o programa que classifique dois valores inteiros quaisquer em ordem crescente. Os valores serão fornecidos pelo usuário.
    valor1 = int(input("Digite o primeiro valor inteiro: "))
    valor2 = int(input("Digite o segundo valor inteiro: "))

    if valor1 < valor2:
        input(f"A ordem crescente dos valores é: {valor1}, {valor2}")
    elif valor1 > valor2:
        input(f"A ordem crescente dos valores é: {valor2}, {valor1}")
    else:
        input("Os valores são iguais.")

def Avaliacao_Pratica_1D():
#D) Construa o programa que calcule o peso ideal de uma pessoa.
# Utilize as seguintes fórmulas:
#- Se homem, o peso ideal é calculado assim: (72,7 . altura) - 58;
#- Se mulher, o peso ideal é calculado assim: (62,1 . altura) - 44,7.
#Analise o problema e verifique quais são os dados que o usuário precisa fornecer (digitar).

    sexo = input("Digite o sexo (M para homem, F para mulher): ")
    altura = float(input("Digite a altura em metros: "))

    if sexo == "M":
        peso_ideal = (72.7 * altura) - 58
    elif sexo == "F":
        peso_ideal = (62.1 * altura) - 44.7
    else:
        input("Sexo inválido.")
        return

    input(f"O peso ideal para uma pessoa do sexo {sexo} com altura {altura} é {peso_ideal:.2f} kg")

#main
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Avaliação\nEscolha\n[a]Questão A\n[b]Questão B\n[c]Questão C\n[d]Questão D\n[e]Exit')

    escolha = str(input('>>> '))
    if escolha == 'a':
        Avaliacao_Pratica_1A()
    elif escolha == 'b':
        Avaliacao_Pratica_1B()
    elif escolha == 'c':
        Avaliacao_Pratica_1C()
    elif escolha == 'd':
        Avaliacao_Pratica_1D()
    elif escolha == 'e':
        print('bye bye')
        break
    else:
        input('escolha entre a, b, c ou d.')

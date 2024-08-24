#Script em python que tem todas as atividades passadas em aula de "Pensamento Computacional" do 1º Semestre.

#Libs usadas
import math

#Nível Básico
#21.08.24
def Login():
#Elabore um programa que verifica se o usuário digitou a senha correta. Mostre a mensagem "senha incorreta" ou "Acesso liberado". Supondo que a senha correta seja 123.
    Senha = '123'

    login = str(input('Digite a senha: '))

    if login == Senha:
        print('Acesso liberado.')
    else:
        print('Acesso Negado.')

def MaiorQCem():
#Faça um programa que leia um valor numérico e mostre uma mensagem
    num1 = float(input('Digite o numero: '))

    if (num1 >= 100):
        print ('número maior que cem')

    elif (num1 <= 100):
        print ('numero é menor que cem')

    elif (num1 == 100):
        print ('os dois sao iguais')
    else:
        print('digire o número')

def NumerosIguais():
#Faça um programa que leia dois valores quaisquer e mostre o maior deles ou mostre a mensagem "os valores são iguas"
    num1 = float(input('primeiro numero: '))
    num2 = float(input('Segundo numero: ' ))

    if (num2 > num1):
        print ('segundo numero é maior que o primeiro numero')

    if (num1 > num2):
        print ('primeiro numero é maior que o segundo numero')

    if (num1 == num2):
        print ('os dois sao iguais')

def NecessidadeDAgua():
# A água é um nutriente essencial. sem ela, o corpo não pode funcionar com perfeição. Cada pessoa precisa de uma quantidade diferente de água para hidratar o corpo. A dose ideal, ou seja, a necessidade diária em litros é calculada através da fórmula: massa (em kg) vezes 0,03. Elabore o programa que realize esse cálculo.
    kg = float(input('Quantos quilos você tem?: '))
    cal = kg * 0.03
    print(f'Você precisa tomar {cal} litros de água')

def ImparPar():
#Elabore um programa que verifica se o valor inteiro fornecido pelo usuário é impar ou par.;
    num = int(input('Digite um número: '))

    if (num%2) == 0:
        resto = num%2
        print(f"Par (número {num} e seu resto é: {resto})")
    else:
        print("Ímpar")

def AprovadoReprovado():
#Programa que calcule a média aritmética de um aluno que realizou duas avaliações. Além do valor da média, inclua na tela de saída uma das mensagens: "Aluno aprovado" ou "Aluno reprovado". Considere que o aluno será aprovado com a média maior ou igual a 5.

    nota = int(input('Digite a nota do aluno: '))
    nota2 = int(input('Digite a segunda nota do aluno: '))

    media = (nota + nota2)/2

    if (media >= 5):
        print ('APROVADO')

    elif (media <= 5):
        print ('REPROVADO')

    elif (media == 5):
        print ('APROVADO')
    else:
        print('digite o número')


# Avaliações Práticas - Básico 1 Semestre

def Avaliacao_Pratica_1A():
#A) Implemente o programa que calcule o volume de uma esfera de raio R. O usuário fornecerá o dado necessário.
    raio = float(input('Digite o raio R : '))
    volume = (4/3) * 3.14 * (raio**2)

    print(f"O volume da efera de raio R {raio} é igual à: {volume:.2f}")

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

    print(f"A distância entre os pontos P({x1}, {y1}) e Q({x2}, {y2}) é {distancia:.2f}")

def Avaliacao_Pratica_1C(): 
# C) Desenvolva o programa que classifique dois valores inteiros quaisquer em ordem crescente. Os valores serão fornecidos pelo usuário.
    valor1 = int(input("Digite o primeiro valor inteiro: "))
    valor2 = int(input("Digite o segundo valor inteiro: "))

    if valor1 < valor2:
        print(f"A ordem crescente dos valores é: {valor1}, {valor2}")
    elif valor1 > valor2:
        print(f"A ordem crescente dos valores é: {valor2}, {valor1}")
    else:
        print("Os valores são iguais.")

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
        print("Sexo inválido.")
        return

    print(f"O peso ideal para uma pessoa do sexo {sexo} com altura {altura} é {peso_ideal:.2f} kg")

#Run
AprovadoReprovado()


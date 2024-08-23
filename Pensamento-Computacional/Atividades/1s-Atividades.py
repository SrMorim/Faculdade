#Script em python que tem todas as atividades passadas em aula de "Pensamento Computacional" do 1º Semestre.
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

def AvaliacaoPratica1A():
#A)Implemente o programa que calcule o volume de uma esfera de raio R. O usuário fornecerá o dado necessário.
    
    raio = float(input('Digite o raio R : '))
    volume = (4/3) * 3.14 * (raio**2)

    print(f"O volume da efera de raio R {raio} é igual à: {volume:.2f}")

def AvaliacaoPratica1B():
#B)

#Run
AvaliacaoPratica1()

# 1.Variáveis e tipos de dados
'''

Crie um programa que solicite ao usuário informações 
como nome, idade e altura, e utilize essas variáveis para exibir uma mensagem personalizada.

'''
'''
nome = input('Digite o seu nome: ')
idade = int(input('Digite a sua idade: '))
altura = float(input('Digite a sua altura: '))
print(f"{nome}, {idade} anos, {altura} metros ")

'''

# 2. Operadores e cálculos
'''

Desenvolva um programa que realize cálculos simples, como a soma, subtração, multiplicação e divisão de dois números inseridos pelo usuário.

'''
'''
numero_1 = float(input('Digite o primeiro número:'))
numero_2 = float(input('Digite o segundo número:'))

operacao = numero_1 + numero_2, numero_1 - numero_2, numero_1 * numero_2, numero_1 / numero_2
print(operacao)

'''
# 3. Manipulação de strings
'''
Escreva um programa que receba uma frase do usuário e conte quantas palavras ela possui. Em seguida, inverta a ordem das palavras na frase.

'''
#frase = input('Digite uma frase:')
#numero_de_letras_sem_espaco = len(frase)
#print("A frase digitada tem: ", numero_de_letras_sem_espaco, "letras")

#frase = input('Digite uma frase:')
#numero_de_letras_com_espaco = len(frase)
#print(f"O número de letras é:{numero_de_letras_com_espaco}")

# 4. Estruturas de decisões e iteração
'''
Implemente um programa que utilize estruturas de decisões (if, else, elif) para determinar se um número inserido pelo usuário é positivo, negativo ou zero. 
Utilize também loops para pedir novos números até que o usuário insira zero.

'''
#numero = float(input('Digite um número:'))

#if numero > 0:
    #print("positivo")
#elif numero < 0:
    #print("negativo")
#else:
    #print("O número é igual a zero")

# 5. Funções e escopos de variáveis
'''
Crie uma função que receba dois números como parâmetros e retorne a soma deles. 
Em seguida, utilize escopos de variáveis para armazenar o resultado e exibi-lo.

'''
def soma_numeros(x,y):
    return x+y

numero_1 = int(input('Digite o primeiro número:'))
numero_2 = int(input('Digite o segundo número:'))

print(f"A soma dos números {numero_1} + {numero_2} é igual:", soma_numeros(numero_1,numero_2))
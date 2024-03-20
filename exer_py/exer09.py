'''
1 Escreva um programa que mostre na tela a mensagem "Olá, Mundo!"

'''
#print("Òlá, mundo!") #Vamos usar o comando (print) para imprimir na tela a mensagem
'''
2)Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boasvindas para ela:
Ex:
Qual é o seu nome? João da Silva
Olá João da Silva, é um prazer te conhecer!

'''
#nome = input('Qual é o seu nome?') #Primeiro vamos criar uma variável para atribuir o valor (nome)
#print(nome) #segundo vamos imprimir na tela a variável (nome) com o nome digitado pelo usuário
#print(f"Olá {nome}, é um prazer te conhecer!") #em seguida vamos imprimir a mensagem de boas vinda com o nome do usuário

'''
3)Crie um programa que leia o nome e o salário de um funcionário, mostrando no
final uma mensagem.
Ex:
Nome do Funcionário: Maria do Carmo
Salário: 1850,45
O funcionário Maria do Carmo tem um salário de R$1850,45 em Junho.

'''
#nome_do_funcionario = input('Digite o seu nome: \n') #Criamos a variável (nome) e pedimos ao usuário que forneça seu nome
#salario = (input("Digite o valor do seu salário: \n")) #Criamos a variável (salario) e pedimos que o usuário o valor do seu salário

#Por último imprimimos a msg com o nome do usuário e o valor so seu salário, para isso usei o modo f-string para colocar tds as váriaveis em um print só
#print(f"Nome do Funcionário: {nome_do_funcionario}\nSalário: {salario}\n O funcionário {nome_do_funcionario} tem um salário {salario} em Junho.")

'''
4)Desenvolva um algoritmo que leia dois números inteiros e mostre o somatório
entre eles.
Ex:
Digite um valor: 8
Digite outro valor: 5
A soma entre 8 e 5 é igual a 13.

'''
#valor_01 = int(input('Digite um valor: ')) #Criamos a variável (valor_01) do tipo inteiro e pedimos ao usuário que digite uma valor
#valor_02 = int(input('Digite outro valor: ')) #Criamos a variável (valor_02) do tipo inteiro e pedimos ao usuário que digite outro valor
#soma = valor_01 + valor_02 #Criamos a variável soma e atribuimos á ela o cálculo dos valores fornecidos pelo usuário
#print("A soma entre",valor_01, "e",valor_02 "È igual á: ",soma,) #Imprimimos a variável (soma) na tela com o resultado da soma dos valores digitados
#pelo usuário

'''
5)Faça um programa que leia as duas notas de um aluno em uma matéria e mostre 
na tela a sua média na disciplina.
Ex: 
Nota 1: 4.5
Nota 2: 8.5
A média entre 4.5 e 8.5 é igual a 6.5

'''
nota_01 = float(input('Digite a primeira nota:')) #Definimos as variáveis (nota_01) e (nota_2) para receber o valor que o usuário vai digitar
nota_02 = float(input('Digite a segunda nota: '))
media = nota_01 + nota_02 / 2 #Criamos a variável média atribuimos á ela o cálculo para saber qual a média do aluno
print(f"A média entre {nota_01} e {nota_02} é igual á {media}")

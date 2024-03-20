'''
Faça um programa que peça uma nota, entre zero e dez. 
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

'''

# 1º passo: Criar a váriavel (nota) e pedir ao usuário que digite uma nota entre 0 e 10.
nota = float(input('Digite uma nota: '))
# 2º passo: Usar um laço de repetição. Nesse caso usamos o laço (while), já que é script que fica se repetindo até o usário informa a nota correta.

while (nota < 10):
    float(input('Não pode ser maior que 0 ou menor que 10 \n tente novamente:'))
    print("Nota Inválida")
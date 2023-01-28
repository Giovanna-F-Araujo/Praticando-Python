# Tarefa Dezenas

#Entrada de dados
numero_str = input("Digite um número inteiro:")

#Cálculo
numero = int(numero_str)
unidade = numero % 10
dezena = numero - unidade
temp = dezena / 10
resultado = int(temp % 10)

#Saída de dados
print("O dígito das dezenas é",resultado)
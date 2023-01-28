'''
Exercício 02 – Ler dois valores para as variáveis A e B e efetuar a
troca dos valores das variáveis, de modo que a variável A passe a
conter o valor de B e a variável B passe a ter o valor de A.
Imprimir os dois valores em tela.

'''
#Entrada de dados 
a = int(input("Digite o valor de a:"))
b = int(input("Digite o valor de b:"))

#Atribuindo
aux = a
a = b
b = aux

#Saída de dados 
print("O valor de a é:",a,"e de b é:",b)

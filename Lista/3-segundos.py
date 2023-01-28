'''
Faça um programa em Python que, dada a quantidade de segundos, "quebre"
esse valor em dias, horas, minutos e segundos. A saída deve estar no formato:
a dias, b horas, c minutos e d segundos. 

Abaixo um exemplo de como deve ser a entrada e saída de dados do programa:

Exemplo:

Entrada de Dados:
Por favor, entre com o número de segundos que deseja converter: 178615

Saída de Dados:
2 dias, 1 horas, 36 minutos e 55 segundos.

'''
#Entrada de dados
total_segundos_str = input("Por favor, entre com o número de segundos que deseja converter: ")

#Cálculo
total_segundos = int(total_segundos_str)
dias = total_segundos // 86400
horas_restantes = total_segundos % 86400
horas = horas_restantes // 3600
segundos_restantes = total_segundos % 3600
minutos = segundos_restantes // 60
segundos = segundos_restantes % 60

#Saída de dados
print(dias,"dias,",horas,"horas,",minutos,"minutos e",segundos,"segundos.")

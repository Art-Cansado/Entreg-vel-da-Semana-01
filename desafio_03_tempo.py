# Solicita o tempo total em segundos e converte para número inteiro
total_segundos = int(input("Digite o tempo em segundos: "))

# Divide o total de segundos por 3600 para descobrir a quantidade de horas
# O operador // retorna apenas a parte inteira da divisão
horas = total_segundos // 3600

# Calcula quantos segundos sobraram depois de retirar as horas
# O operador % retorna o resto da divisão
resto = total_segundos % 3600

# Divide os segundos restantes por 60 para descobrir os minutos
minutos = resto // 60

# Calcula os segundos que sobraram depois de retirar os minutos
segundos = resto % 60

# Exibe o tempo convertido em horas, minutos e segundos
print(f"{horas} hora(s), {minutos} minuto(s) e {segundos} segundo(s)")

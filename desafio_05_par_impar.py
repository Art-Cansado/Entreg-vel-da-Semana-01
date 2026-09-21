# Solicita um número inteiro ao usuário
numero = int(input("Digite um número inteiro: "))

# O operador % calcula o resto da divisão
# Se o resto da divisão por 2 for igual a 0, o número é par
if numero % 2 == 0:
    # Executado quando o número é divisível por 2
    print("O número é par.")

else:
    # Executado quando o número não é divisível por 2
    print("O número é ímpar.")

# Solicita a primeira nota e converte o valor para número decimal
nota_1 = float(input("Digite a primeira nota: "))

# Solicita a segunda nota e converte o valor para número decimal
nota_2 = float(input("Digite a segunda nota: "))

# Solicita a terceira nota e converte o valor para número decimal
nota_3 = float(input("Digite a terceira nota: "))

# Soma as três notas e divide por 3 para calcular a média
media = (nota_1 + nota_2 + nota_3) / 3

# Exibe a média com duas casas decimais
print(f"Média: {media:.2f}")

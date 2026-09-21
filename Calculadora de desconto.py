# Solicita o preço do produto e converte para número decimal
preco = float(input("Digite o preço do produto: R$ "))

# Solicita a porcentagem de desconto
percentual_desconto = float(input("Digite o percentual de desconto: "))

# Calcula o valor do desconto
# Divide a porcentagem por 100 para transformá-la em valor decimal
desconto = preco * (percentual_desconto / 100)

# Calcula o preço final retirando o desconto do preço original
preco_final = preco - desconto

# Exibe o preço final com duas casas decimais
print(f"Preço final: R$ {preco_final:.2f}")

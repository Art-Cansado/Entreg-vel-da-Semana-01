# Solicita o valor total da compra e converte para número decimal
valor_compra = float(input("Digite o valor da compra: R$ "))

# Solicita o valor que o cliente pagou e converte para número decimal
valor_pago = float(input("Digite o valor pago: R$ "))

# Calcula o troco subtraindo o valor da compra do valor pago
troco = valor_pago - valor_compra

# Exibe o valor do troco com duas casas decimais
print(f"Troco: R$ {troco:.2f}")

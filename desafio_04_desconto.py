preco = float(input("Digite o preço do produto: R$ "))
percentual_desconto = float(input("Digite o percentual de desconto: "))

desconto = preco * (percentual_desconto / 100)
preco_final = preco - desconto

print(f"Preço final: R$ {preco_final:.2f}")
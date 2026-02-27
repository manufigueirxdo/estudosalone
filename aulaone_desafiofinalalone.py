nomedoproduto = input("Qual é o nome do produto?")
valordoproduto = float(input("Quanto ele custa?"))
quantidade = int(input("Quantos você comprou?"))
valorinvestido = valordoproduto * quantidade
lucro = valordoproduto * 1.5
print(f"Você comprou {quantidade}")
print(f"de {nomedoproduto}")
print(f"e investiu um total de R${valorinvestido}.")
print(f"Para obter um lucro de 50%, você precisa cobrar R${lucro}")
print(f"do {nomedoproduto}.")


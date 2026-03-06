produto = float(input("Qual é o valor do produto?"))
frete = float(input("Quanto custa o frete?"))
montagem = float(input("Quanto custa a montagem?"))
total_venda = produto + frete + montagem

for parcela in range(1,13):
    valor_dividido = total_venda / parcela
    print(f"{parcela}x de R${valor_dividido}")
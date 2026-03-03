valor_compra = float(input("Qual é o valor da compra?"))
quilometragem = float(input("Quantos km de distância fica sua residência?"))

if valor_compra >= 500:
    frete = 0
elif quilometragem <= 50:
    frete = 20
else:
    frete = 50

valor_total = valor_compra + frete

print(f"O valor total da sua compra é de R${valor_total}")

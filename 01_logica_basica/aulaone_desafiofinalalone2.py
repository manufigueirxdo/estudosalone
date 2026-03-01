totalinvestido = float(input("Quanto você investiu nesse anúncio?"))
vendasporanuncio = int(input("Quantas vendas foram feitas com esse anúncio?"))
valorvenda = float(input("Quanto custou cada venda feita a partir desse anúncio?"))

faturamentototal = vendasporanuncio * valorvenda
lucroliquido = faturamentototal - totalinvestido
roi = ((lucroliquido / totalinvestido) * 100)

print(f"O seu faturamento foi de R${faturamentototal}")
print(f"o seu lucro real foi de R${lucroliquido}")
print(f"e o seu ROI foi de {roi}%")

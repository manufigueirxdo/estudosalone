valor = float(input("Qual é o valor do projeto em Dólar?"))
for cotacao in range(5, 11):
    total = valor * cotacao
    print(f"Com o Dólar a {cotacao}, você ganha {total}")
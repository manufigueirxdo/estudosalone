nomedocliente = input("Como você se chama?")
idadedocliente = int(input("Qual é sua idade?"))
valordoproduto = float(input("Qual é o valor do produto que você deseja comprarW"))
limitedocartao = float(input("Qual é o limite do seu cartão?"))
taxadefrete = valordoproduto * 0.05
valorbruto = valordoproduto + taxadefrete

if valorbruto > 1000:
    valorliquido = valorbruto - 50
else:
    valorliquido = valorbruto

print(f"O valor líquido a pagar é de R${valorliquido}")

if idadedocliente >= 18 and limitedocartao >= valorliquido:
        print("Compra aprovada!")
else:
        print("Compra recusada por idade ou limite insuficiente!")

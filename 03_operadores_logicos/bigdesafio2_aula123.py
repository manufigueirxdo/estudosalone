distancia_corrida = float(input("Qual é a distância da corrida?"))
quantidade_corrida = int(input("Quantas corridas foram feitas hoje?"))

bruto_corrida = distancia_corrida * 2.50

if bruto_corrida > 30:
    taxa_corrida = bruto_corrida * 0.10
else:
    taxa_corrida = bruto_corrida * 0.20

ganholiquido = bruto_corrida - taxa_corrida

print(f"O seu ganho liquído nessa corrida é de R${ganholiquido}")

if ganholiquido >= 20 and quantidade_corrida < 10:
    print("Status: Corrida Recomendada!")
else:
    print("Status: Corrida Recusada pelo algoritmo.")
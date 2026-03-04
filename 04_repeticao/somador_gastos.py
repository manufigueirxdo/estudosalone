total_gasto = 0
novo_gasto = -1
while novo_gasto !=0:
    novo_gasto = float(input("Digite o valor do gasto (ou 0 para sair"))
    total_gasto = total_gasto + novo_gasto
    print(f"O total dos seus gastos foi de R${total_gasto}")
    
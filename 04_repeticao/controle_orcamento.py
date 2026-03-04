orcamento = float(input("Qual o orçamento total do projeto?"))
despesa = -1

while despesa !=0:
    despesa = float(input("Digite o valor da despesa (ou 0 para sair)."))
    if despesa == 0:
        print("Não há despesas!")
    elif despesa > orcamento:
        print("Despesa recusada! Orçamento estourado!")
    else:
        orcamento = orcamento - despesa
        print(f"Despesa aprovada. Saldo atual de R${orcamento}")
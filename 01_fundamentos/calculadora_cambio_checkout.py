valor_emdolar = float(input("Qual é valor da compra em dolár?"))
taxa_cambio = 5.10
valor_emreal = valor_emdolar * taxa_cambio
taxa_iof = valor_emreal * 0.06
valor_bruto = valor_emreal + taxa_iof
print(f"O total da sua compra em real é de R${valor_bruto}.")
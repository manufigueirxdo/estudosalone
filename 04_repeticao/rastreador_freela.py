valor_hora = float(input("Quanto custa a sua hora?"))
total_horas = 0
horas_hoje = -1

while horas_hoje != 0:
    horas_hoje = float(input("Quantas horas você trabalhou hoje? (Digite 0 para fechar o mês.)"))
    total_horas = total_horas + horas_hoje

valor_total = total_horas * valor_hora

print(f"Seu total de horas trabalhadas foi de {total_horas}")
print(f"O valor total a receber é de R${valor_total}")
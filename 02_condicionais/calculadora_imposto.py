salario_bruto = float(input("Quanto é o seu salário?"))

if salario_bruto <= 2000:
    imposto = 0.

elif salario_bruto > 2000 and salario_bruto <= 5000:
    imposto = salario_bruto * 0.10

else:
    imposto = salario_bruto * 0.20

salario_liquido = salario_bruto - imposto

print(f"Seu imposto é de R${imposto}")
print(f"Seu salário é de R${salario_liquido}")


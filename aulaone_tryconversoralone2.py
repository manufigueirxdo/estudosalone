salario_bruto = float(input("Quanto é o seu salário?"))
imposto = 0.10
valor_total = salario_bruto * imposto
salario_liquido = salario_bruto - valor_total
print(f"Seu imposto é de R${valor_total}")
print(f"E seu salário líquido é no valor e de R${salario_liquido}")
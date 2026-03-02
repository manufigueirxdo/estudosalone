salario_base_mensal = float(input("Qual é o seu salário base mensal?"))
dias_trabalhados = int(input("Por quantos dias você trabalhou?"))
valor_diario = salario_base_mensal / 30
salario_proporcional = valor_diario * dias_trabalhados
deposito_fgts = salario_proporcional * 0.08
print(f"O seu salário proporcional é de R${salario_proporcional}")
print(f"O valor a ser recolhido do seu FGTS é de R${deposito_fgts}")

nome_do_funcionario = (input("Nome do funcionário?"))
salario_bruto = float(input("Qual o salário bruto dele(a)?"))

desconto = salario_bruto * 0.11
salario_liquido = salario_bruto - desconto

e_maior = salario_liquido > 2000.00
print(f"O salário líquido é maior que R$2000.00? {e_maior}")

salario_cliente = float(input("Qual é o valor do seu salário?"))
parcela = float(input("Qual o valor da parcela que você deseja pagar?"))
limite_parcela = salario_cliente * 0.30
if salario_cliente > 2000 and parcela <= limite_parcela:
    print("Emprestimo aprovado!")
else:
    print("Emprestimo recusado!")

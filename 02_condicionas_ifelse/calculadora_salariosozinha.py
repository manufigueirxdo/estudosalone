nomedofuncionario = input("Identificação do funcionário?")
salariobase = float(input("Quanto é o salário do funcionário?"))
if salariobase <= 0:
    print("Salário inválido!")
else:
    descontoinss = salariobase * 0.11
    salarioliquido = salariobase - descontoinss
    if salariobase < 1500:
        bonus = salarioliquido + 100
        print(f"Você ganhou um bônus de R$100! Seu salário líquido é de R${bonus}")
    else:
        print(f"Seu salário líquido é de R${salarioliquido}")

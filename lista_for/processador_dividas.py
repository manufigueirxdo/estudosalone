dividas = [100, 450.50, 89.90, 1500, 32]
for boleto in dividas:
    multa = boleto * 0.10
    valor_total = boleto + multa
    print(f"Boleto original: R${boleto:.2f} | Boleto com multa: R${valor_total:.2f}")
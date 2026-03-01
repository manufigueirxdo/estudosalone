totaldecaixas = int(input("Quantas caixas há no depósito?"))
capacidadedocaminhao = 20
caminhaocheio = totaldecaixas // capacidadedocaminhao
caixassobrando = totaldecaixas % capacidadedocaminhao
print(f"Serão necessários {caminhaocheio} caminhões cheios.")
print(f"Ficarão {caixassobrando} caixas para a próxima viagem.")

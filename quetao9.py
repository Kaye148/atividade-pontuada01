
renda_mensal = float(input("Digite a renda mensal do solicitante: "))
emprestimo_total = float(input("Digite o valor total do empréstimo: "))
num_prestacoes = int(input("Digite o número de prestações desejado: "))


valor_max_emprestimo = renda_mensal * 10
valor_max_prestacao = renda_mensal * 0.30
valor_prestacao = emprestimo_total / num_prestacoes


if emprestimo_total <= valor_max_emprestimo:
    if valor_prestacao <= valor_max_prestacao:
        print("Empréstimo CONCEDIDO.")
        print(f"Valor da prestação: R$ {valor_prestacao:.2f}")
    else:
        print("Empréstimo NEGADO.")
        print("Motivo: o valor da prestação excede 30% da renda mensal.")
else:
    print("Empréstimo NEGADO.")
    print("Motivo: o valor total do empréstimo excede 10x a renda mensal.")
    if valor_prestacao > valor_max_prestacao:
        print("Motivo: o valor da prestação excede 30% da renda mensal.")

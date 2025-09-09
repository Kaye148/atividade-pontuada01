produto = input("informe o nome do produto: ")
quantidade = int(input("infome a quantidade: "))
preco_unitario = float(input("informe o preco: "))

total = quantidade * preco_unitario

if quantidade <= 5:
    desconto = 0.02
elif quantidade <=10:
    desconto = 0.03
else:
    desconto = 0.05

desconto = total * desconto
total_a_pagar = total -desconto
print(f"produto: {produto}")
print(f"total: R$ {total:.2f}")
print(f"desconto: R$ {desconto:.2f}")
print(f"total a pagar: R$ {total_a_pagar:.2f}")


combustivel = input("Digite o tipo de combustível (A para Álcool, G para Gasolina): ").strip().upper()
litros = float(input("Digite a quantidade de litros vendidos: "))
preco_alcool = 3.79
preco_gasolina = 6.59

if combustivel == "A":
    if litros <= 25:
        desconto = 0.10  
    else:
        desconto = 0.20 
    preco_bruto = litros * preco_alcool
elif combustivel == "G":
    if litros <= 25:
        desconto = 0.15
    else:
        desconto = 0.30  
    preco_bruto = litros * preco_gasolina
else:
    print("Tipo de combustível inválido.")
    desconto = 0
    preco_bruto = 0
valor_desconto = preco_bruto * desconto
preco_final = preco_bruto - valor_desconto
if preco_bruto > 0:
    print(f"Preço sem desconto: R$ {preco_bruto:.2f}")
    print(f"Desconto aplicado: R$ {valor_desconto:.2f}")
    print(f"Valor a ser pago: R$ {preco_final:.2f}")

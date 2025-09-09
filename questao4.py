kg_morango = float(input("digite a quantidade de morangos: " ))
kg_maca = float(input("digite a quantidade de maças: " ))

if kg_morango <= 5:
    preco_morango = 2.50
else:
    preco_morango = 2.20
if kg_maca <= 5:
    preco_maca = 1.80
else:
    preco_maca = 1.50

total_morango = kg_morango * preco_morango
total_maca = kg_maca * preco_maca
total_kg = kg_morango + kg_maca
total_preco = total_morango + total_maca

if total_kg > 10 or total_preco > 15:
    total_preco *= 0.90
print(f"valor para pagar:  R$ {total_preco:.2f}")

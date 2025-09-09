operacoes = input("informe uma operação +,-,*ou/:" )
A = int(input("digite o valor de A: "))
B = int(input("digite o valor de B: "))

if operacoes == '+':
    resultados = A + B
elif operacoes == '-':
    resultados = A - B
elif operacoes == "*":
    resultados = A * B
elif operacoes == "/":
    if B != 0:
        resultados = A / B
print(f"resultados: {resultados}")

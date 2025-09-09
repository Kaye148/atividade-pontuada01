nota1 = float(input("digite a primeira nota:" ))
nota2 = float(input("digite a segunda nota: "))
nota3 = float(input("digite a terceira nota: "))
nota4 = float(input("digite a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) /4

print(f"media do aluno :{media:.2f}")

if media >= 6.0:
    print("parabens aluno aprovado")
elif 4.1 <= media < 6.0:
    print("voce esta em recuperação")
else:
    print("você foi reprovado")
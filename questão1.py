import os
os.system("cls")

A = int(input("digite um numero: "))
B = int(input("digite um numero: "))
C = int(input("digite um numero: "))

soma = A + B

if soma < C:
    print(f"a soma entra {A} e {B} é menor que  {C}")

else:
    print(f"a soma entra {A} e {B} é maior que  {C}")

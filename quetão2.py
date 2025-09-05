nome = input("digite seu nome: ")
sexo = input("informe o sexo(M/F): ")
estado_civil = str("informe seu estado civil: ")
if sexo == "f" and estado_civil == "casada":
    tempo_casada = input("digite o tempode casada(em anos): ")
else:
    tempo_casada = "não se aplica"
print(f"nome:{nome}")
print(f"sexo:{sexo}")
print(f"estado civil:{estado_civil}")
print(f"tempo de casada:{tempo_casada}")





nome = input("Digite o nome: ")
sexo = input("Digite o sexo (M/F): ")
estado_civil = input("Digite o estado civil: ")

if sexo == 'F' and estado_civil == 'CASADA':
    tempo_casada = input("Digite o tempo de casada (em anos): ")
else:
    tempo_casada = "Não se aplica"

print(f"Nome: {nome}")
print(f"Sexo: {sexo}")
print(f"Estado Civil: {estado_civil}")
print(f"Tempo de casada: {tempo_casada}")

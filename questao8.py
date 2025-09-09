
cor = input("Digite a cor do CD (Verde, Azul, Amarelo, Vermelho): ").strip().lower()

if cor == "verde":
    print("O preço do CD é R$ 10,00")
elif cor == "azul":
    print("O preço do CD é R$ 20,00")
elif cor == "amarelo":
    print("O preço do CD é R$ 30,00")
elif cor == "vermelho":
    print("O preço do CD é R$ 40,00")
else:
    print("Cor inválida. Por favor, digite uma das seguintes: Verde, Azul, Amarelo, Vermelho.")
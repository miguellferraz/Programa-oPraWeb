from random import randint

ns = randint(1, 10)

try:
    while True:
        tentativa = int(input("\nDigite um número entre 1 e 10: "))

        if tentativa == ns:
            print("\nO computador escolheu:", ns)
            print("Você escolheu:", tentativa)
            print("Você Acertou!")
            break
        elif tentativa > 10:
            print("\nÉ pra digitar um número entre 1 e 10.")
            print("Tente Novamente!")
            ns = randint(1, 10)
        else:
            print("\nO computador escolheu:", ns)
            print("Você escolheu:", tentativa)
            print("Tente Novamente!")
            ns = randint(1, 10)

except ValueError:
    print("Erro: Você deve digitar apenas números válidos.")


   

try:
    numerador = float(input("Digite o numerador: "))
    denominador = float(input("Digite o denominador: "))
    
    resultado = numerador / denominador
    print(f"Resultado da divisão: {resultado}")

except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")

except ValueError:
   print("Erro: Você deve digitar apenas números válidos.")

finally:
    print("Operação finalizada. Obrigado por usar o programa.")

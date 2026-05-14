val1 = int(input("Digite valor 1: "))
val2 = int(input("Digite valor 2: "))

operacao = input("Digite a operação (*, /, +, -): ")
result = None

if operacao == "*":
    result = val1 * val2
elif operacao == "/":
    result = val1 / val2
elif operacao == "+":
    result = val1 + val2
elif operacao == "-":
    result = val1 - val2

print("Resultado da operação:" ,result)


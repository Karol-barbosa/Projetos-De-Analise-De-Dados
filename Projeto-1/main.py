from mean_var_std import calculate

# Teste com lista de 9 números
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]

result = calculate(numbers)

print("Resultados da função calculate():")
for key, value in result.items():
    print(f"{key}: {value}")

# Teste do ValueError
try:
    calculate([1, 2, 3]) 
except ValueError as e:
    print("\nErro capturado corretamente:")
    print(e)

numeros = []
for i in range(3):
    n = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(n)

# lista multiplicada
numeros_x2 = [num * 2 for num in numeros]

print("Lista original:", numeros)
print("Lista multiplicada por 2:", numeros_x2)

print("Soma da lista original:", sum(numeros))
print("Soma da lista multiplicada:", sum(numeros_x2))
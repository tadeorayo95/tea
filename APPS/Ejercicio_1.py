lista = []
while True:
    valor = input("Introduce un número (o 'fin' para terminar): ")
    if valor .lower() in "fin":
        break
    try:
        lista.append(int(valor))
    except ValueError:
        print("Valor introducido incorrecto. Intenta de nuevo. . .")

print("La suma de los números es de: {}" .format(sum(lista)))
print("La cantidad de números introducidos es de {}" .format(len(lista)))
print("El promedio de valores ha sido de{}" .format(sum(lista)/len(lista)))
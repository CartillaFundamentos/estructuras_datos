# Ejercicio No. 65: Lista con elementos únicos.

lista1 = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
lista2 = []

# processing
for n in lista1:
    if n not in lista2:
        lista2.append(n) 

# output
print("La lista con elementos únicos:") 
print(lista2)
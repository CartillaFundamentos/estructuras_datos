# Ejercicio No. 66: Calculadora básica con menú 2.

from math import log

print("1 ---> Suma (x + y)")
print("2 ---> Resta (x - y)")
print("3 ---> Multiplicación (x * y)")
print("4 ---> División (x + y)")
print("5 ---> Potencia (x^y)")
print("6 ---> Logaritmo (base = x, argumento = y)")

# input
x = float(input("Ingrese el valor de x: "))
y = float (input("Ingrese el valor de y: "))
opcion = input("Operación que desea realizar: ")

# processing
operaciones = {"1":x+y, "2":x-y, "3":x*y, "4":x/y, "5":x**y, "6":log(y, x)}

# output
print(operaciones[opcion])
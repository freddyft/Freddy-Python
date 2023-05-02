
# Programa que me permita calcular la tabla de multiplicar de cualquier numero entero dada por el usuario.
# Debe calcular la tabla desde el 0 hasta el 12.

def tablaMultiplicar(n1, n2):
    return str(n1) + " * " + str(n2) + " = " +  str(n1 * n2)

x = int(input("Ingrese un valor: "))

for i in range(0, 13):
    print( tablaMultiplicar(x, i))


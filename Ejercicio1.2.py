
# Programa que toma las 3 notas de un estudiante y diga la nota final del curso.
#Tener en cuenta que la primera y segunda nota valen 30% de la nota final. La tercera nota vale 40%

def calcularNota(nota1, nota2, nota3):
    return (nota1 * 0.3) + (nota2 * 0.3) + (nota3 * 0.4)

nota1 = float(input("Ingrese la nota de su primera evaluación: "))
nota2 = float(input("Ingrese la nota de su segunda evaluación: "))
nota3 = float(input("Ingrese la nota de su tercera evaluación: "))

notafinal = calcularNota(nota1, nota2, nota3)

print("La nota final del alumno es de: ", notafinal)




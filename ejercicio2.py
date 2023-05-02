
#Programa que calcule el IVA de una compra, el cual tiene un porcentaje de 19%.

def IVA(producto, iva):
    return (producto + iva)
producto = float(input("Ingrese el precio de su compra: "))
iva = producto * 0.19

data1 = IVA(producto, iva)

print("El valor de su compra sin IVA es de: ", producto)
print("Sumandole el IVA, da un total de: ", data1)

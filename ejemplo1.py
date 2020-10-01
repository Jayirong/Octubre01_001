#Ingresar 2 números como int
a=int(input("Ingrese un número: "))
b=int(input("Ingrese otro número: "))
#operaciones matemáticas
suma=a+b
multi=a*b
print("La suma de "+str(a)+" con el número "+str(b)+" es igual a: "+str(suma))
print("La multiplicación de "+str(a)+" con el número "+str(b)+" es igual a: "+str(multi))
#creamos una condición
if (a>b):
    print("El número "+str(a)+" es mayor que "+str(b))
elif (a<b):
    print("El número "+str(b)+" es mayor que "+str(a))
else:
    print("Los números son iguales")
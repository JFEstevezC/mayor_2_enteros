a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))

if a == b:
    mayor = ("Los números son iguales")
elif a > b:
    mayor = ("El número mayor es " + str(a))
else: 
    mayor = ("El número mayor es " + str(b))
print(mayor)

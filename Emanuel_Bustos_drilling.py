lista_nombres = ["Harry Houdini", "Newton", "David Blaine", "Hawking", "Messi", "Teller", "Einstein", "Pele", "Juanes"]

magos = []
cientificos = []
otros = []

for nombre in lista_nombres:
    if nombre in ["Harry Houdini", "David Blaine", "Teller"]:
        magos.append(nombre)
    elif nombre in ["Newton", "Hawking", "Einstein"]:
        cientificos.append(nombre)
    else:
        otros.append(nombre)

def hacer_gradioso():
    for contador in range(len(magos)):
        magos[contador] = "El gran" + magos[contador]
    

def imprimir_nombres(lista):
    for nombre in lista:
        print(nombre)

print("*" * 20 + " Primer requerimiento, lista completa de nombres " + "*" * 20)
print(lista_nombres)
print("*" * 20 + " Todos los nombres antes de ser modificados "+ "*" * 20)
imprimir_nombres(lista_nombres)
print("*" * 80)
print("*" * 20 + "Segundo requerimiento, Imprimir Magos Grandiosos" + "*" * 20)
hacer_gradioso()
imprimir_nombres(magos)
print("*" * 80)
print("*" * 20 + "Tercer requerimiento, Imprimir Nombres de los Cientificos" + "*" * 20)
imprimir_nombres(cientificos)
print("*" * 80)
print("*" * 20 + "Cuarto requerimiento, Imprimir los Nombres Restantes" + "*" * 20)
imprimir_nombres(otros)
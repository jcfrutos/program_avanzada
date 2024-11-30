
print("Selecciona la operación que deseas realizar:")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

while True:
    op = input("Ingresa el número de la operación (1/2/3/4): ")
    op = int(op)
    if op not in [1, 2, 3, 4]:
        print("Ingresa el valor correcto")
        break

    a = input("ingrese un numero: ")

    try:
        a = int(a)
    except ValueError:
        print("no es un valor valido")
        continue
    b = input("ingrese otro numero: ")
    try:
        b = int(b)
    except ValueError:
        print("no es un valor valido")
        continue    
    
    resultado = ""

    if op == 1:
        resultado = f"""Resultado = {a + b}"""

    if op == 2:
        resultado = f"""Resultado = {a - b}"""

    if op == 3:
        resultado = f"""Resultado = {a * b}"""

    if op == 4:
        resultado = f"""Resultado = {a / b}"""

    print(resultado)

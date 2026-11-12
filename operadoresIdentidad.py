## OPERADORES DE IDENTIDAD

# "is" - Verifica si dos variables se refieren al mismo objeto en memoria
# "is not" - Verifica si dos variables no se refieren al mismo objeto en memoria

a = 3.56
b = 3.56
print(f"a = {a}, b = {b}")

# is

c = a is b
print(f"a is b = {c}")

# is not

c = a is not b
print(f"a is not b = {c}")

#--------------------------------
print("\n -------")

a = 3.56
b = a 

c = a is b
print(f"a is b = {c}")

c = a is not b
print(f"a is not b = {c}")

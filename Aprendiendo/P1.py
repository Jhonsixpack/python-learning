
#Práctica Print e Input

# Crear un "Diario de un Astronauta" 
# usando la función print para mostrar mensajes en la consola.

print("Diarario de un Astronauta\n")
ingresar = input("Desea ingresar al diario? (si/no): ")

def ingresar_fecha():
    return input("Ingresa la fecha (dd/mm/aaaa): ")

def ingresar_actividad():
    return input("Ingrese la actividad realizada: ")

seguir = "si"

while seguir == "si":
    fecha = ingresar_fecha()
    actividad = ingresar_actividad()

    print(f"\nFecha: {fecha}\nActividad: {actividad}\n")

    seguir = input("Desea ingresar otra actividad? (si/no): ")
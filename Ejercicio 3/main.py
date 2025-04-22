from NaveEspacial import NaveEspacial
from GranRallyEspacial import GranRallyEspacial

# Ejemplo de uso
naves = [
    NaveEspacial("Cometa Veloz", 50, 5, 10),
    NaveEspacial("Titán del Cosmos", 100, 8, 20),
    NaveEspacial("GX-200", 70, 6, 15),
    NaveEspacial("Estrella Fugaz", 40, 4, 5),
    NaveEspacial("GX-100", 60, 7, 12),
    NaveEspacial("Nave Aurora", 80, 10, 25),
]

rally = GranRallyEspacial(naves)

print("1. Ordenar por nombre ascendente y longitud descendente:")
rally.ordenar_por_nombre_y_longitud()
for nave in rally.naves:
    print(nave)

print("\n2. Información de 'Cometa Veloz' y 'Titán del Cosmos':")
rally.mostrar_info_naves(["Cometa Veloz", "Titán del Cosmos"])

print("\n3. Cinco naves con mayor cantidad de pasajeros:")
rally.cinco_mayor_pasajeros()

print("\n4. Nave que requiere mayor cantidad de tripulación:")
rally.nave_mayor_tripulacion()

print("\n5. Naves cuyo nombre comienza con 'GX':")
rally.naves_comienzan_con("GX")

print("\n6. Naves que pueden llevar seis o más pasajeros:")
rally.naves_seis_o_mas_pasajeros()

print("\n7. Nave más pequeña y más grande:")
rally.nave_mas_pequena_y_grande()
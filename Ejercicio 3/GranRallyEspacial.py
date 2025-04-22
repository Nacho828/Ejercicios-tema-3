class GranRallyEspacial:
    def __init__(self, naves):
        self.naves = naves

    def ordenar_por_nombre_y_longitud(self):
        self.naves.sort(key=lambda nave: (nave.nombre, -nave.longitud))

    def mostrar_info_naves(self, nombres):
        for nave in self.naves:
            if nave.nombre in nombres:
                print(nave)

    def cinco_mayor_pasajeros(self):
        top_cinco = sorted(self.naves, key=lambda nave: nave.pasajeros, reverse=True)[:5]
        for nave in top_cinco:
            print(nave)

    def nave_mayor_tripulacion(self):
        nave = max(self.naves, key=lambda nave: nave.tripulantes)
        print(nave)

    def naves_comienzan_con(self, prefijo):
        for nave in self.naves:
            if nave.nombre.startswith(prefijo):
                print(nave)

    def naves_seis_o_mas_pasajeros(self):
        for nave in self.naves:
            if nave.pasajeros >= 6:
                print(nave)

    def nave_mas_pequena_y_grande(self):
        nave_pequena = min(self.naves, key=lambda nave: nave.longitud)
        nave_grande = max(self.naves, key=lambda nave: nave.longitud)
        print("Nave más pequeña:")
        print(nave_pequena)
        print("Nave más grande:")
        print(nave_grande)

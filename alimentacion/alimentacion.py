from abc import ABC, abstractmethod


class Mercancia(ABC):
    """Clase base abstracta para cualquier mercancia de alimentacion."""

    def __init__(self, marca, modelo):
        # Atributos privados para aplicar encapsulacion.
        self.__marca = marca
        self.__modelo = modelo

    def get_marca(self):
        return self.__marca

    def set_marca(self, marca):
        self.__marca = marca

    def get_modelo(self):
        return self.__modelo

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def mostrar_info(self):
        """Metodo comun que las clases hijas sobrescriben."""
        return f"Marca: {self.__marca} | Modelo: {self.__modelo}"

    @abstractmethod
    def calcular_coste(self):
        """Cada tipo de mercancia calcula su coste de forma distinta."""
        pass


class Fruta(Mercancia):
    """Mercancia de tipo fruta."""

    def __init__(self, marca, modelo, procedencia, kilos, precio_kilo):
        super().__init__(marca, modelo)
        self.__procedencia = procedencia
        self.__kilos = kilos
        self.__precio_kilo = precio_kilo

    def get_procedencia(self):
        return self.__procedencia

    def set_procedencia(self, procedencia):
        self.__procedencia = procedencia

    def get_kilos(self):
        return self.__kilos

    def set_kilos(self, kilos):
        self.__kilos = kilos

    def get_precio_kilo(self):
        return self.__precio_kilo

    def set_precio_kilo(self, precio_kilo):
        self.__precio_kilo = precio_kilo

    def calcular_coste(self):
        # La fruta se calcula directamente por peso y precio por kilo.
        return self.__kilos * self.__precio_kilo

    def mostrar_info(self):
        return (
            f"[FRUTA] {super().mostrar_info()} | "
            f"Procedencia: {self.__procedencia} | "
            f"Kilos: {self.__kilos:.2f} | "
            f"Precio/kg: {self.__precio_kilo:.2f} EUR | "
            f"Coste: {self.calcular_coste():.2f} EUR"
        )


class Carne(Mercancia):
    """Mercancia de tipo carne."""

    def __init__(self, marca, modelo, animal, kilos, precio_kilo, coste_refrigeracion):
        super().__init__(marca, modelo)
        self.__animal = animal
        self.__kilos = kilos
        self.__precio_kilo = precio_kilo
        self.__coste_refrigeracion = coste_refrigeracion

    def get_animal(self):
        return self.__animal

    def set_animal(self, animal):
        self.__animal = animal

    def get_kilos(self):
        return self.__kilos

    def set_kilos(self, kilos):
        self.__kilos = kilos

    def get_precio_kilo(self):
        return self.__precio_kilo

    def set_precio_kilo(self, precio_kilo):
        self.__precio_kilo = precio_kilo

    def get_coste_refrigeracion(self):
        return self.__coste_refrigeracion

    def set_coste_refrigeracion(self, coste_refrigeracion):
        self.__coste_refrigeracion = coste_refrigeracion

    def calcular_coste(self):
        # La carne suma el coste extra de refrigeracion al coste por peso.
        return (self.__kilos * self.__precio_kilo) + self.__coste_refrigeracion

    def mostrar_info(self):
        return (
            f"[CARNE] {super().mostrar_info()} | "
            f"Animal: {self.__animal} | "
            f"Kilos: {self.__kilos:.2f} | "
            f"Precio/kg: {self.__precio_kilo:.2f} EUR | "
            f"Refrigeracion: {self.__coste_refrigeracion:.2f} EUR | "
            f"Coste: {self.calcular_coste():.2f} EUR"
        )
                            

def main():
    # Lista comun de mercancias: permite recorrerlas de forma polimorfica.
    mercancias = [
        Fruta("Frutasol", "Manzana Golden", "Asturias", 120, 1.35),
        Fruta("TropicalFresh", "Platano", "Canarias", 80, 1.80),
        Carne("Carnicas Norte", "Lomo fresco", "Cerdo", 55, 6.40, 18.50),
        Carne("Ganadera Sur", "Filete premium", "Ternera", 35, 12.75, 22.00),
    ]

    print("GESTION DE MERCANCIAS DE ALIMENTACION")
    print("-" * 45)

    for mercancia in mercancias:
        print(mercancia.mostrar_info())


if __name__ == "__main__":
    main()

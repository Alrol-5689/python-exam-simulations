from pathlib import Path


# Archivo donde se guardan los libros para que los datos sean persistentes.
ARCHIVO_LIBROS = Path("libros.txt")

# Datos iniciales que se escriben si libros.txt todavia no existe.
LIBROS_PREDETERMINADOS = [
    {
        "nombre": "Los pilares de la tierra",
        "identificador": "1049",
        "encargado": "Mario",
    },
    {
        "nombre": "El nombre de la rosa",
        "identificador": "2234",
        "encargado": "Luis",
    },
    {
        "nombre": "El perfume",
        "identificador": "3187",
        "encargado": "Angela",
    },
]


def crear_archivo_predeterminado():
    """Crea libros.txt con algunos libros de ejemplo."""
    with ARCHIVO_LIBROS.open("w", encoding="utf-8") as archivo:
        for libro in LIBROS_PREDETERMINADOS:
            archivo.write(
                f"{libro['nombre']};{libro['identificador']};{libro['encargado']}\n"
            )


def cargar_libros():
    """
    Lee los libros desde libros.txt.

    Cada linea del archivo usa el formato:
    nombre;identificador;persona_encargada
    """
    if not ARCHIVO_LIBROS.exists():
        crear_archivo_predeterminado()

    libros = []

    with ARCHIVO_LIBROS.open("r", encoding="utf-8") as archivo:
        for linea in archivo:
            datos = linea.strip().split(";")

            # Se ignoran lineas vacias o con formato incorrecto.
            if len(datos) != 3:
                continue

            nombre, identificador, encargado = datos
            libros.append(
                {
                    "nombre": nombre,
                    "identificador": identificador,
                    "encargado": encargado,
                }
            )

    return libros


def mostrar_libros(libros):
    """Muestra los libros en pantalla con un formato claro."""
    print("LISTADO DE LIBROS")
    print("=" * 60)

    if not libros:
        print("No hay libros registrados.")
        return

    for numero, libro in enumerate(libros, start=1):
        print(f"Libro {numero}")
        print(f"  Nombre:        {libro['nombre']}")
        print(f"  Identificador: {libro['identificador']}")
        print(f"  Encargado:     {libro['encargado']}")
        print("-" * 60)


def main():
    """Funcion principal del programa."""
    libros = cargar_libros()
    mostrar_libros(libros)


if __name__ == "__main__":
    main()

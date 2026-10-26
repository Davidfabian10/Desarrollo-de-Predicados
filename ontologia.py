hechos_animales = {
    "perro": {
        "caracteristicas": ("es_mamifero", "ladra", "es_domestico"),
        "es_mamifero": True,
        "ladra": True,
        "es_domestico": True,
        "aulla": False,
        "es_salvaje": False,
        "vive_mar": False,
        "tiene_espiraculo": False,
        "tiene_branquias": False,
        "aleta_vertical": False
    },
    "lobo": {
        "caracteristicas": ("es_mamifero", "aulla", "es_salvaje"),
        "es_mamifero": True,
        "ladra": False,
        "es_domestico": False,
        "aulla": True,
        "es_salvaje": True,
        "vive_mar": False,
        "tiene_espiraculo": False,
        "tiene_branquias": False,
        "aleta_vertical": False
    },
    "delfin": {
        "caracteristicas": ("es_mamifero", "vive_mar", "tiene_espiraculo"),
        "es_mamifero": True,
        "ladra": False,
        "es_domestico": False,
        "aulla": False,
        "es_salvaje": True,
        "vive_mar": True,
        "tiene_espiraculo": True,
        "tiene_branquias": False,
        "aleta_vertical": False
    },
    "tiburon": {
        "caracteristicas": ("vive_mar", "tiene_branquias", "aleta_vertical"),
        "es_mamifero": False,
        "ladra": False,
        "es_domestico": False,
        "aulla": False,
        "es_salvaje": True,
        "vive_mar": True,
        "tiene_espiraculo": False,
        "tiene_branquias": True,
        "aleta_vertical": True
    }
}

vinculos = [
    (animal, "requiere", caracteristica)
    for animal, datos in hechos_animales.items()
    for caracteristica in datos["caracteristicas"]
]

vinculos += [
    ("es_domestico", "opuesto_de", "es_salvaje"),
    ("perro", "emparentado_con", "lobo"),
    ("delfin", "comparte_habitat_con", "tiburon")
]

# Reglas logicas
def es_perro(c):
    return c.get("es_mamifero") and c.get("ladra") and c.get("es_domestico")

def es_lobo(c):
    return c.get("es_mamifero") and c.get("aulla") and c.get("es_salvaje")

def es_delfin(c):
    return c.get("es_mamifero") and c.get("vive_mar") and c.get("tiene_espiraculo")

def es_tiburon(c):
    return c.get("vive_mar") and c.get("tiene_branquias") and c.get("aleta_vertical")


def evaluar_base_conocimiento():
    print("--- EVALUACION DE REGLAS Y HECHOS ---")
    for nombre, datos in hechos_animales.items():
        print(f"\nEvaluando al ejemplar: [{nombre}]")
        print(f"Caracteristicas (Tupla): {datos['caracteristicas']}")

        # Aplicacion de reglas
        if es_perro(datos):
            print("Resultado logico: Es un perro")
        elif es_lobo(datos):
            print("Resultado logico: Es un lobo")
        elif es_delfin(datos):
            print("Resultado logico: Es un delfin")
        elif es_tiburon(datos):
            print("Resultado logico: Es un tiburon")
        else:
            print("Resultado logico: No se pudo clasificar con las reglas actuales")


def mostrar_vinculos():
    print("\n--- VINCULOS ENTRE CONCEPTOS ---")
    for sujeto, relacion, objeto in vinculos:
        print(f"{sujeto} --{relacion}--> {objeto}")


if __name__ == "__main__":
    evaluar_base_conocimiento()
    mostrar_vinculos()
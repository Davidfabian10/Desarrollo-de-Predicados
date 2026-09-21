dominio = {
    "Estudiantes": {
        "David": {
            "materias": ["Programacion"],
            "Carrera": "IngSistemas",
            "Materias_aprobadas": ["Programacion"] 
        },
        "Fabian": {
            "materias": ["Programacion", "Calculo"],
            "Carrera": "IngIndustrial",
            "Materias_aprobadas": []
        }
    },
    "Profesores": {
        "Yamamoto": {
            "materias": ["Programacion"]
        },
        "Laura": {
            "materias": ["Calculo"]
        }
    },
    "Materias": {
        "Programacion": {
            "Aula": "Salon206"
        },
        "Calculo": {
            "Aula": "Salon306"
        }
    }
}

#Predicados
# 1 - Estudiante(x) = "x es estudiante"
def estudiante(x):
    for est, datos in dominio["Estudiantes"].items():
        if est == x:
            return True
    return False

# 2 - Profesor(x) = "x es profesor"
def profesor(x):
    for prof, datos in dominio["Profesores"].items():
        if prof == x:
            return True
    return False

# 3 - Inscrito(x, m) = "x esta inscrito en la materia m"
def inscrito(x, m):
    for est, datos in dominio["Estudiantes"].items():
        if est == x:
            for materia in datos["materias"]:
                if materia == m:
                    return True
    return False

# 4 - Imparte(p, m) = "el profesor p imparte la materia m"
def imparte(p, m):
    for prof, datos in dominio["Profesores"].items():
        if prof == p:
            for materia in datos["materias"]:
                if materia == m:
                    return True
    return False

# 5 - PerteneceCarrera(x, c) = "el estudiante x pertenece a la carrera c"
def pertenece_carrera(x, c):
    for est, datos in dominio["Estudiantes"].items():
        if est == x:
            if datos["Carrera"] == c:
                return True
    return False

# 6 - AsignadoAula(m, a) = "la materia m se imparte en el aula a"
def asignado_aula(m, a):
    for materia, datos in dominio["Materias"].items():
        if materia == m:
            if datos["Aula"] == a:
                return True
    return False

# 7 - Aprobado(x, m) = "el estudiante x aprobo la materia m"
def aprobado(x, m):
    for est, datos in dominio["Estudiantes"].items():
        if est == x:
            for materia in datos["Materias_aprobadas"]:
                if materia == m:
                    return True
    return False

if __name__ == "__main__":
    # 1
    print("1 - Estudiante(x) = x es estudiante")
    print("Estudiante(David) =", estudiante("David"))
    print("Estudiante(Yamamoto) =", estudiante("Yamamoto"))
    print("-" * 50)

    # 2 
    print("2 - Profesor(x) = x es profesor")
    print("Profesor(Laura) =", profesor("Laura"))
    print("Profesor(Fabian) =", profesor("Fabian"))
    print("-" * 50)

    # 3
    print("3 - Inscrito(x, m) = x esta inscrito en la materia m")
    print("Inscrito(David, Programacion) =", inscrito("David", "Programacion"))
    print("Inscrito(David, Calculo) =", inscrito("David", "Calculo"))
    print("-" * 50)

    # 4
    print("4 - Imparte(p, m) = el profesor p imparte la materia m")
    print("Imparte(Yamamoto, Programacion) =", imparte("Yamamoto", "Programacion"))
    print("Imparte(Laura, Programacion) =", imparte("Laura", "Programacion"))
    print("-" * 50)

    # 5
    print("5 - PerteneceCarrera(x, c) = el estudiante x pertenece a la carrera c")
    print("PerteneceCarrera(David, IngSistemas) =", pertenece_carrera("David", "IngSistemas"))
    print("PerteneceCarrera(David, IngIndustrial) =", pertenece_carrera("David", "IngIndustrial"))
    print("-" * 50)

    # 6
    print("6 - AsignadoAula(m, a) = la materia m se imparte en el aula a")
    print("AsignadoAula(Programacion, Salon206) =", asignado_aula("Programacion", "Salon206"))
    print("AsignadoAula(Programacion, Salon306) =", asignado_aula("Programacion", "Salon306"))
    print("-" * 50)

    # 7
    print("7 - Aprobado(x, m) = el estudiante x aprobo la materia m")
    print("Aprobado(David, Programacion) =", aprobado("David", "Programacion"))
    print("Aprobado(Fabian, Programacion) =", aprobado("Fabian", "Programacion"))
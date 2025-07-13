cursos = {
    "C001": "Programación Básica",
    "C002": "Introducción a Python",
    "C003": "Bases de Datos"
}
inscripciones = {}

def menu():
    while True:
        try:
            menu=int(input('''
                        1.- Inscribir Alumno
                        2.- Consultar Inscripcion
                        3.- Cancelar Inscripcion
                        4.- Salir
                        '''))
            if menu == 1:
                inscribir_alumno()
            elif menu == 2:
                consultar_inscripcion()
            elif menu == 3:
                cancelar_inscripcion()
            elif menu == 4:
                print("Saliendo...")
            else:
                print("Ingrese opcion del 1 al 4")
        except Exception:
            print("Opcion invalida")
            break

def inscribir_alumno():
    print("Para inscribirse se necesitan los siguientes datos: ")
    alumno=input("Ingrese su nombre: ")
    curso=input("Ingrese codigo del curso: ").upper()
    while True:
        codigo = input("Ingrese código de confirmación: ")
        if validar_codigo(codigo):
            print("Código válido.")
            break
        else:
            print("Código inválido, inténtalo otra vez.")
    inscripciones[alumno] = {"curso": curso, "codigo": codigo}
    print("Inscripción registrada.")


def validar_codigo(codigo):
    largo_ok = len(codigo) >= 6
    mayus = False
    digito = False
    for c in codigo:
        if c.isupper():
            mayus = True
        if c.isdigit():
            digito = True
    sin_espacios = " " not in codigo
    if largo_ok and mayus and digito and sin_espacios:
        return True
    else:
        return False

def consultar_inscripcion():
    while True:
        nombre = input("Ingrese el nombre del alumno a consultar: ")
        if nombre in inscripciones:
            print("Curso:", inscripciones[nombre]["curso"])
            print("Código:", inscripciones[nombre]["codigo"])
            break
        else:
            print("Nombre no encontrado, ingrese nuevamente")

def cancelar_inscripcion():
    while True:
        nombre = input("Ingrese el nombre del alumno a cancelar: ")
        if nombre in inscripciones:
            del inscripciones[nombre]
            print("Inscripcion eliminada correctamete!")
            break
        else:
            print("Ingrese nombre valido")

menu()
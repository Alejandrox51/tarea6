def ingresar_evaluacion():
    while True:
        print('Por favor, ingrese su evaluación en una escala del 1 al 5:')
        calificacion = input()
        if calificacion.isdigit():
            calificacion = int(calificacion)
            if 1 <= calificacion <= 5:
                print('Ingrese sus comentarios:')
                comentarios = input()
                evaluacion = f'Calificación: {calificacion}, Comentarios: {comentarios}'
                with open("evaluaciones.txt", 'a') as archivo:
                    archivo.write(f'{evaluacion}\n')
                break
            else:
                print('Por favor, ingrese un valor entre 1 y 5.')
        else:
            print('Por favor, ingrese una calificación numérica válida.')

def verificar_resultados():
    print('Evaluaciones recientes:')
    with open("evaluaciones.txt", "r") as archivo:
        print(archivo.read())

def menu_principal():
    while True:
        print('Seleccione una opción:')
        print('1: Ingresar evaluación')
        print('2: Verificar evaluaciones')
        print('3: Salir')
        opcion = input()

        if opcion.isdigit():
            opcion = int(opcion)
            if opcion == 1:
                ingresar_evaluacion()
            elif opcion == 2:
                verificar_resultados()
            elif opcion == 3:
                print('Saliendo del programa.')
                break
            else:
                print('Por favor, ingrese un número entre 1 y 3.')
        else:
            print('Por favor, ingrese un número de opción válido.')

if __name__ == "__main__":
    menu_principal()

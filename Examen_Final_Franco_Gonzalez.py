import csv 
import random
import math

sueldos = []

trabajadores = [
    {'nombre': 'Juan Perez'},
    {'nombre': 'Maria Garcia'},
    {'nombre': 'Carlos Lopez'},
    {'nombre': 'Ana Martinez'},
    {'nombre': 'Pedro Rodriguez'},
    {'nombre': 'Laura Hernandez'},
    {'nombre': 'Miguel Sanchez'},
    {'nombre': 'Isabel Gomez'},
    {'nombre': 'Francisco Diaz'},
    {'nombre': 'Elena Fernandez'},
]

def asignar_sueldo():
    for trabajador in trabajadores:
        sueldo = random.randint(300000, 2500000)
        sueldos.append(sueldo)
    print(sueldos)

def clasificacion():
    print('Clasificación de Sueldo')
    print('Sueldo Bajo: ')
    for trabajador, sueldo in zip(trabajadores, sueldos):
        if sueldo<800000:
            print(f"Nombre: {trabajador['nombre']},Sueldo: ${sueldo}")
    print('Sueldo entre $800.000 y $2.000.000:')
    for trabajador, sueldo in zip(trabajadores, sueldos):
        if 800000 <= sueldo <= 2000000:
            print(f"Nombre: {trabajador['nombre']},Sueldo: ${sueldo}")
    print('Sueldo superior a $2.000.000:')
    for trabajador, sueldo in zip(trabajadores, sueldos):
        if sueldo > 2000000:
            print(f"Nombre: {trabajador['nombre']}, Sueldo: ${sueldo}")

def ver_estadisticas():
    sueldo_max = max(sueldos)
    sueldo_min = min(sueldos)
    sueldo_promedio = sum(sueldos) / len(sueldos)
    sueldo_geom = math.exp(sum(math.log(sueldo) for sueldo in sueldos) / len(sueldos))
    print(f'Sueldo más alto: {sueldo_max}')
    print(f'Sueldo más bajo: {sueldo_min}')
    print(f'Sueldo promedio: {sueldo_promedio}')
    print(f'Media Geométrica de sueldo: {sueldo_geom}')

def reporte_sueldo():
    with open('archivo_trab.csv', 'w', newline='') as archivo_trab:
        escritor = csv.writer(archivo_trab)
        encabezado = ['Nombre Empleado', 'Sueldo Base', 'Desc Salud', 'Desc AFP', 'Sueldo Bruto']
        escritor.writerow(encabezado)
        for trabajador, sueldo in zip(trabajadores, sueldos):
            salud = (sueldo * 7) / 100
            afp = (sueldo * 12) / 100
            sueldo_bruto = sueldo - salud - afp
            escritor.writerow([trabajador['nombre'], sueldo, int(salud), int(afp), int(sueldo_bruto)])
            print(f"Nombre:{trabajador['nombre']}, Sueldo: ${sueldo}, Salud: {salud},AFP: {afp}, Sueldo Total: {sueldo_bruto}")

def salir_programa():
    print('Desarrollado por Franco González')
    print('RUT: 21.897.832-0')
    print('Finalizando Programa....')

def menu():
    while True:
        print('1) Asignar sueldo')
        print('2) Clasificación de sueldo')
        print('3) Estadísticas')
        print('4) Reporte de sueldo')
        print('5) Salir')
        opc = int(input('Selecciona una opción: '))
        if opc == 1:
            asignar_sueldo()
        elif opc == 2:
            clasificacion()
        elif opc == 3:
            ver_estadisticas()
        elif opc == 4:
            reporte_sueldo()
        elif opc == 5:
            salir_programa()
            break
        else:
            print('Selecciona Una Opción Correcta')
menu()
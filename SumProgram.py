'''
UNIVERSIDAD NACIONAL AUTÓNOMA DE MÉXICO
FACULTAD DE ESTUDIOS SUPERIORES ARAGÓN

INGENIERÍA EN COMPUTACIÓN
ASIG. 2508 DISEÑO Y ANALISIS DE ALGORITMOS
PROF. PERÉZ SANCHEZ HIRAM ENMANUEL

DATOS DEL ALUMNO
ALUMNO: HERRERA GARCIA RICARDO ALFREDO
N. CTA: 41310655-7

PROGRAMA: SUMA DOS NÚMEROS DEL 1 AL 100 MEDIANTE UN MÉTODO
'''

def sum(x, y):
    return x + y

numero1 = 0;
while numero1 <= 0 or numero1 > 100:
    numero1 = int(input("Introduce el primer número a sumar (mayor a cero y menor a 100): "))

numero2 = 0;
while numero2 <= 0 or numero2 > 100:
    numero2 = int(input("Introduce el segundo número a sumar (mayor a cero y menor a 100): "))

suma = sum(numero1, numero2)
print("La suma de los dos números es:", suma)

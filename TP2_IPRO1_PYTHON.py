#by
#█████████████████████████████████████
#██▀▄─██▄─▄███▄─▄▄─█▄─▀─▄█▄─▀─▄█▄─▄▄─█
#██─▀─███─██▀██─▄█▀██▀─▀███▀─▀███─▄█▀█
#▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄█▄▄▀▄▄█▄▄▀▄▄▄▄▄▀

#-------------------------------------
#Casos de Estudio
#-------------------------------------

regimen = input("¿De que régimen eres?(diurno/vespertino):")
nota_alumno = float(input("Ingresa tu nota(0/10): "))

if regimen == "diurno":
    if nota_alumno >= 3.5:
        print("El alumno debe rendir examen.")
    else:
        print("El alumno ha reprobado.")
elif regimen == "vespertino":
    if nota_alumno >= 6:
        print("El alumno está exento.")
    elif nota_alumno >= 3.5:
        print("El alumno debe rendir examen.")
    else:
        print("El alumno ha reprobado.")
else:
    print("Régimen inválido")

#------------------------------------------
#EJERCICIOS
#------------------------------------------
                     #explicacion
    
#!= :es el operador de desigualdad, que compara dos valores y devuelve

#== :es el operador de igualdad, que compara dos valores y devuelve True si son iguales y False si son diferentes.

#>= :es el operador de mayor o igual, que compara dos valores y devuelve True si el primero es mayor o igual al segundo, y False en caso contrario.

#<= :es el operador de menor o igual, que compara dos valores y devuelve True si el primero es menor o igual al segundo, y False en caso contrario.

#True y False: son valores booleanos que representan verdadero y falso, respectivamente. Estos valores se utilizan comúnmente en las expresiones lógicas para determinar si una afirmación es verdadera o falsa.

#or :es un operador lógico que devuelve True si al menos una de las expresiones que se evalúan es verdadera. Si ambas expresiones son falsas, entonces el resultado es False.

# and : es otro operador lógico en Python. Evalúa a True si y solo si ambas expresiones a su izquierda y derecha son verdaderas.

# not :es un operador lógico que invierte el valor de la expresión que se evalúa. Si la expresión es verdadera, entonces el resultado es False. Si la expresión es falsa, entonces el resultado es True.

#-------------------------------------------

r = 10
s = 0

resultado = (r != 10) or not (s == -r) or not((True or r >= 10) and not (s <= 0 and True))

print(resultado)

#---------------------------------------------
#A
"""
(v <= 0) and (w > 0)

#B
(v != w) and (v != z) and (w != z)

#C
(v != 0) and (w <= z)

#D
(v < w < z) or (z < w < v)

#E
(v == w) or (z >= 0 and (v >= 0) != (z >= 0))"""
#------------------------------------------------

#Analice el siguiente código en Python:

"""1. clave = "iprog1"
2. contraseña = input("Introduce la contraseña: ")
3. if clave == contraseña:
4. print("La contraseña coincide")
5. else:
6. print("La contraseña NO coincide")
● ¿Cuándo se visualizará en la pantalla el mensaje “coincide”?
● Si ingresa en la variable contraseña iProg1, ¿Qué mensaje se verá en la pantalla?
● Mejore la sentencia en la línea 3 utilizando alguna función que salve la situación anterior.
● ¿Qué sucede si ingresa un número?"""

#El mensaje va a coincidir si en la entrada(input) coincide con la varible clave

#Si ingresa iProg1 en el input, saldrá un mensaje "La contraseña NO coincide"

#para eso usamos la función "lower()" que convertirá la contraseña en minuscula y esto hará coincidir con la variable clave

contraseña = input("Introduce la contraseña: ")
#if clave == contraseña.lower():
    


#si ingresa un número, saltará un error en Python

#---------------------------------------------
edad_cliente = int(input("La edad del cliente es: "))
fichas_a_comprar = int(input("¿Cuantas fichas compará?: "))

if 4 <= edad_cliente < 7:
    precio = 35 * 0.8
    fichas_a_comprar += 5
elif 7 <= edad_cliente < 10:
    precio = 35 * 1.15
else:
    print("Edad fuera de rango")
    precio = 0
if precio > 0:
    total = fichas_a_comprar * precio
    print("El monto total de fichas es:", total, "pesos")

#----------------------------------------------

num1 = float(input("Ingresa un número: "))
num2 = float(input("Ingresa un segundo número: "))
num3 = float(input("Ingresa un tercer número: "))

if num1 < num2 < num3:
    print("Los número estan decreciente")
elif num1 > num2 > num3:
    print("Los números estan decreciente")
else:
    print("Los números estan desordenados")

#-----------------------------------------------

#si ingreso "a" en la primera entrada, me saltará un error o nada.

#si ingreso "v" en la segunda entrada, me mostrará el siguiente mensaje: la mezcla y de Rojo y Verde producen Amarrillo.

#me mostrará otro mensaje para elegir otro color:

#si ingreso "v" otra vez en la segunda entrada, me mostrará el siguiente mensaje: La mezcla de Azul y Verde producen Cian.

#y por ultimo me mostrará un mensaje diciendo "hasta la proxima"

#------------------------------------------------

                        #EDAD:12,18

#si la edad ingresada por la variable "edad" es mayor que cero y edad es menor o igual a 12, entonces mostrará: "Es un niño"
#si la edad ingresada es mayor que 12 y edad es menor o igual a18, mostrará: "Es un adolescente".
#si la edad ingresada por la variable es mayor que 18 y edad es menor o igual a 80, entonces mostrará: "Es un adulto".
# y si edad es mayor que 80 entonces es un anciano.

"""si ingreso 12, mostrará que es un niño.
    
    si ingreso 18, me mostrará que es un adolescente"""

#----------------------------------------------------------

                        #NUMERO:-5,0,10

"""si ingreso -5, me mostrará: "negativo"
    -5

    si ingreso 0, me mostrará 0.


    si ingreso 10, me mostrará positivo.
    10 """

#---------------------------------------------------------

anio = int(input("Ingrese el año: "))

if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
    print(anio, "es un año bisiesto")
else:
    print(anio, "no es un año bisiesto")

#--------------------------------------------------------

            #Sentencia Selectiva simple

edad = int(input("Ingresa tu edad: "))

if edad < 0:
    print("Error, la edad es negativa")
else:
    if edad <= 17:
        print("Sos menor de edad")
    else:
        print("Sos mayor de edad")

#--------------------------------------------------------

            #Sentencia encadenada

edad = int(input("Ingresa tu edad: "))

if edad < 0:
    print("Error, la edad es negativa")
elif edad <= 17:
    print("Sos menor de edad")
else:
    print("Sos mayor de edad")

#-------------------------------------------------------

        #Sentencia Selectiva anidada

numero = int(input("Ingrese un número entero: "))
if numero % 2 == 0:
    if numero % 4 == 0:
        print(numero, "es múltiplo de cuatro (y de dos)")
    else:
        print(numero, "es múltiplo de dos")
else:
    print(numero, "no es múltiplo de dos")

#-----------------------------------------------------

        #con estructura if elif else

numero = int(input("Ingrese un número entero: "))
if numero == 0 or numero % 4 == 0:
    print(numero, "es múltiplo de cuatro (y de dos)")
elif numero % 2 == 0:
    print(numero, "es múltiplo de dos")
else:
    print(numero, "no es múltiplo de dos")

#-----------------------------------------------------

# El usuario ingresa la fecha actual en formato “día, DD/MM".
curso = input("Ingrese el nombre del curso: ")
fechas = input("Ingrese día y fecha actual en formato: día, DD/MM ")


# Dias en una lista
dias = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]

# Desempaquetar entrada
dia_semana, fecha_dia_mes = fechas.split(", ")
dia, mes = map(int, fecha_dia_mes.split("/"))

# Validar que el día esté entre 1 y 31
if dia < 1 or dia > 31:
    print("El día debe estar entre 1 y 31")
else:
    print("El día es válido")

# Validar que el mes esté entre 1 y 12
if mes < 1 or mes > 12:
    print("El mes no existe")
else:
    print("El mes es válido")
    
# Validar que el día de la semana esté en la lista de días
if dia_semana.lower() not in dias:
    print("El día de la semana ingresado no es válido")
else:
    print("El día de la semana es válido")

nivel = input("Indique el nivel de inglés (Inicial, Intermedio o Avanzado): ")

if nivel in ["Inicial", "Intermedio", "Avanzado"]:
    examenes = input("¿Hubo exámenes? (s/n): ")
    if examenes.lower() == "s":
        aprobados = int(input("Indique la cantidad de alumnos aprobados: "))
        no_aprobados = int(input("Indique la cantidad de alumnos no aprobados: "))
        porcentaje_aprobados = aprobados / (aprobados + no_aprobados) * 100
        print(f"El porcentaje de alumnos aprobados es: {porcentaje_aprobados}%")
    else:
        print("No hubo exámenes.")
else:
    print("El nivel de inglés indicado no tiene exámenes.")

#practica hablada

if curso == "Práctica Hablada":
    asistencia = int(input("Ingrese el porcentaje de asistencia a clase: "))
    if asistencia > 50:
        print("Asistió la mayoría")
    else:
        print("No asistió la mayoría")

if curso == "Inglés para Viajeros" and dia == 1:
    print("Comienzo de nuevo ciclo")
if curso in ["Inicial", "Intermedio", "Avanzado"]:
    aprobaron = int(input("Ingrese el número de alumnos que aprobaron el examen: "))
    desaprobaron = int(input("Ingrese el número de alumnos que desaprobaron el examen: "))
    total_alumnos = aprobaron + desaprobaron
    porcentaje_aprobados = aprobaron / total_alumnos * 100
    print(f"Porcentaje de aprobados: {porcentaje_aprobados}%")

#-------------------------------------------------------------------------

destino = input("Escriba su destino (Europa, África, Egipto u otro país de África): ")
frecuente = input("¿Viajas frecuentemente? (sí o no): ")
descuento = 0
hotel = False
kilometros = 0


if destino == "Europa":
    if frecuente == "sí":
        descuento = 0.17
        hotel = True
    else:
        descuento = 0.0
        hotel = False
elif destino == "África":
    if frecuente == "sí":
        descuento = 0.17
        hotel = True
    else:
        descuento = 0.0
        hotel = False
elif destino == "Egipto":
    if frecuente == "sí":
        descuento = 0.5
        hotel = False
    else:
        descuento = 0.0
        hotel = False
else:
    if frecuente == "sí":
        kilometros = True
    else:
        kilometros = False
        hotel = False

if descuento > 0:   
    print(f"Tenes descuento del {descuento*100}% en su pasaje.")
if hotel:
    print("Tenes una noche gratis en un hotel.")
if kilometros:
    print("Tenes derecho a una cantidad de kilómetros gratuitos para su siguiente viaje.")

#--------------------------------------------------------------------------------

nuevo = input("¿Sos nuevo? (s/n): ")
if nuevo.lower() == "s":
    print("llena la ficha de inscripción.")
    tiene_beca = input("¿Tenes una beca? (s/n): ")
    if tiene_beca.lower() == "n":
        valor_incorporacion = float(input("Ingrese el valor de incorporación: "))
        # Procesar pago de incorporación
    else:
        print("Usted está exento al pago de incorporación.")
else:
    print("Sos un estudiante antiguo.")
    fecha_limite = input("Ingresa la fecha límite de pago de matrícula en formato dd/mm/aaaa: ")
    fecha_pago = input("Ingresa la fecha de pago de matrícula en formato dd/mm/aaaa: ")
    if fecha_pago <= fecha_limite:
        print("Pago de matrícula recibido. Puede proceder a inscribir sus asignaturas.")
    else:
        motivo_solicitud = input("Ingrese el motivo por el cual no pudo pagar la matrícula antes de la fecha límite: ")
        if motivo_solicitud == "motivo aceptado":
            print("Solicitud aceptada. Puede proceder a inscribir sus asignaturas pagando la multa correspondiente.")
        else:
            print("Solicitud rechazada. Usted queda fuera del proceso de inscripción y perderá los valores que hubiera cancelado.")
#-----------------------------------------------------------------------------------



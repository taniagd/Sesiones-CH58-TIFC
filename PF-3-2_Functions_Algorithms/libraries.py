#El código importa un módulo para trabajar con fechas, crea una fecha específica y luego imprime esa fecha y el número que representa su día de la semana.

import datetime #Importación de módulo. 
"""
Indica que queremos usar una herramienta llamada "datetime". 
Este módulo contiene clases y funciones especiales para manejar fechas y horas.
"""

date = datetime.date(2017,10,1) #Se crea un objeto de fecha.
"""
datetime.date() es una función que está dentro del módulo datetime. Se usa para crear un objeto que representa una fecha específica.
Se le pasan tres argumentos en este orden: año, mes y día.
2017 es el año.
10 es el mes de octubre.
1 es el día primero.

El resultado de esta función es un objeto date que almacena esta fecha.
Lo guardamos en una variable llamada date.
"""

print(date) #Imprimir la fecha
#Esta línea imprime el contenido de la variable date que creamos. El objeto date ya sabe cómo presentarse de forma legible.

print(date.weekday()) #Obtener el día de la semana
"""
date.weekday() es un método (una función que pertenece a un objeto) del objeto date.
Este método te devuelve el día de la semana como un número entero.

Los días de la semana se numeran de la siguiente manera:
Lunes es 0
Martes es 1
Miércoles es 2
Jueves es 3
Viernes es 4
Sábado es 5
Domingo es 6
Como el 1 de octubre de 2017 fue un domingo, el método weekday() devuelve el número 6.

"""
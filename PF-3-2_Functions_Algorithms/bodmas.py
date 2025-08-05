# En la mayoría de los lenguajes de programación, la aritmética sigue el orden de ejecución BODMAS (siglas en inglés) :
"""
B - Brackets (Paréntesis, corchetes, llaves)
O - Orders (Orden de potencias o raíces)
D - Division (División)
M - Multiplication (Multiplicación)
A - Addition (Suma)
S - Substraction (Resta)

Nota: Cuando hay una multiplicación y una división, o una suma y una resta, en la misma expresión,
se resuelven de izquierda a derecha.
"""

#Ejemplo 1:
result1 = 3 + 5 * 8
result2 = (3 + 5) * 8
result3 = 3 + (5 * 8)

"""
result1: Primero se ejecuta la multiplicación (5*8) = 40. Luego, se realiza la suma 3 + 40 = 43.
result2: Los paréntesis son los de máxima prioridad, entonces se calcula primero (3+5) = 8.
Después, se realiza la multiplicación 8 * 8 = 64.
result3: Se resuleven primero los paréntesis (5*8) = 40. Luego se suma 3 + 40= 43
"""

#Ejemplo 2:
resulta = 12 - 6 / 3
resultb = (12 - 6) / 3
resultc = 12 - (6 / 3)

"""
resulta: Primero se realiza la división (6/3)= 2. Luego se hace la resta 12-2=10.
resultb: Los paréntesis se resuelven primero (12-6)=6. Luego se hace la división 6/3=2
resultc: Los paréntesis se resuleven primero, son máxima prioridad (6/3)=2, luego se hace la resta 12-2=10
"""
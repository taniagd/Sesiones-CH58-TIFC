limit = 12 
#Variable limit con valor de 12. Este será el tope que no queremos rebasar.
counter = 1 
#Variable contador, que iniciará en uno. Esta variable llevará la cuenta en cada vuelta del bucle
while counter < limit: #Bucle while con condición establecida: Valor del counter menor al límite
    print(counter) #Si la condición es verdadera, entonces se imprime el valor del counter
    counter = counter + 1 
#Esta línea hace que el bucle avance, le dice al programa, en cada vuelta, que tome el valor actual y le sume 1, paraque sea el nuevo valor
#Si eliminas u omites el +1, entrarás a un bucle infinito. Este +1 es esencial para que el bucle avance


"""
Aquí una explicación un poco más extensa del funcionamiento del while:
El programa llegará a la línea 5, donde comienza el bucle while y evaluará la condición establecida:
counter < limit, es decir, que el contador sea menor al límite establecido, que es 12, cosa que declaramos
en la línea 1, con la variable limit. 
Como la condición es verdadera, el código dentro del bucle while se ejecutará y en la primera vuelta
del bucle se va a imprimir el valor actual del counter, que es 1, posterior, en la línea 7, se actualizará
el contador, pues ahora valdrá 2.
El bucle termina esa primera vuelta y regresa al inicio del bucle para reevaluar la condición.
La condición sigue siendo counter<limit, ahora counter vale 2 y el límite sigue siendo 12.
Este proceso se repetirá una y otra vez, hasta llegar a que el valor del counter sea 12, sin embargo,
en ese momento ya no se cumplirá la condición de que counter<limit (12<12), pues 12 no es menor a 12, 
la condición se vuelve falsa, el bucle se detiene. 
"""
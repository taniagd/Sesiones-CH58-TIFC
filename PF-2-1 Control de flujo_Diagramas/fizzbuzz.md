# Ejercicio FizzBuzz

## Descripción

Imprime los números del 1 hasta el 20, excepto:

- Si el número es divisible por 3, imprime **"Fizz"** en lugar del número.
- Si el número es divisible por 5, imprime **"Buzz"** en lugar del número.
- Si el número es divisible tanto por 3 como por 5, imprime **"FizzBuzz"** en lugar del número.
- Si no se cumple ninguna de estas condiciones, imprime el número.

---

## Errores lógicos

Los errores lógicos ocurren cuando un programa no se comporta como se espera, aunque no tenga errores de sintaxis, es decir, el código “corre”, pero da resultados incorrectos o inesperados. 

- No generan mensajes de error del compilador o intérprete.
- Suelen ser difíciles de detectar porque la aplicación parece funcionar.
- Provocan resultados inesperados o incorrectos.

---

## Errores lógicos comunes en FizzBuzz

- **Orden de prioridad:**  
  El error lógico más común es no verificar primero si un número es divisible por 15 (tanto 3 como 5). Si no se hace así, por ejemplo el número 15 podría imprimir "Fizz" en lugar de "FizzBuzz".

- **Condiciones exclusivas:**  
  Es importante que las estructuras de decisión se aseguren que para cada número solo una acción sea posible: imprimir **Fizz**, **Buzz**, **FizzBuzz** o el número.

- **Rango del bucle:**  
  El ciclo debe ejecutarse mientras el número sea menor o igual a 20, para asegurar que el programa termine correctamente.

---

## Diagrama de flujo

Aquí puedes insertar el diagrama de flujo que explica el proceso visualmente:

![Diagrama de flujo](../images/TIFC1-PF-2-1-2%20-%20Fizzbuzz.jpg)

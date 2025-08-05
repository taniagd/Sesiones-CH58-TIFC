# Función para decir "Hello!"
def print_hello_world():
  print("Hello world - from a function!")

"""
def es la palabra clave para definir una nueva función en python
print_hello_world es el nombre que se le dio a la función. Hay que tratar de ser descriptivos.
Los paréntesis vacíos indican que la función no necesita recibir ninguna información para funcionar.
Los : indican el inicio del bloque de código de la función
print en la función integrada en python para imprimir mensaje en la consola
"Hello world - from a function!" es una cadena de texto (str) que será el mensaje que se imprimirá. 
"""

# Función que retorna la frase "Hello <name>"
def hello_name(name):
  response = "Hello " + name
  return response
"""
La función se llama hello_name. Entre paréntesis, tiene un parámetro llamado name, lo que significa que esta
función necesita de un valor para poder operar. 
En esta línea response = "Hello " + name, se crea una variable llamada response, donde se combina una cadena de
texto ("Hello") con el valor que se le pasó a la función en el parámetro "name". Por ejemplo, si se pasa el
nombre "Zuri", esta línea creará la cadena de texto: "Hello Zuri".
return es una palabra clave que le dice a la función que termine y devuelva un valor. En este caso, 
la función devuelve el contenido de la variable response.
Esto es útil porque puedes guardar el resultado de la función en otra variable o usarlo en otra parte de tu programa.

"""

# Función que realiza una operación matématica sencilla: Suma de dos números
def add(num1, num2):
    response = num1 + num2
    return response

"""
La función se llama add y tiene dos parámetros: num1 y num2. Es decir, necesita de dos valores numéricos
para operar. 
response = num1 + num2, se crea la variable "response" y se suman los dos números que le fueron pasados,
el resultado se almacena en esta variable.
en return response se devuelve el resultado de la suma.
"""
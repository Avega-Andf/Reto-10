# Reto 10

### 1. Desarrollar un algoritmo que calcule el promedio de un arreglo de reales.

<details><summary>codigo</summary><p>

``` python
def crearlista(e:int)->list:
    """
    Crea una lista de números flotantes.

    Args:
    e (int): Un entero que indica la cantidad de elementos que se deben ingresar en la lista.
    
    returns:
    list: Una lista de números flotantes.
    
    """
    lista = [] #Se crea una lista vacia
    for i in range(e): #El tamaño lo decidira la variable "e"
        n = float(input("Ingrese un numero para la lista: ")) # Se le preguntara al usuario por cada elemento que ingresara
        lista.append(n) # Agrega ese elemento
    return lista # Regresa la lista

def calcularpromedio(lista)->float:
    """
    Calcula el promedio de los elementos de una lista de flotantes
    
    Args:
    lista: Una lista a la cual se le hallara el promedio a sus elementos
    
    returns:
    promedio: El promedio de los elementos de la lista
    
    """
    prom = 0 # Inicia la variable en cero, para no alterar la suma
    n = len(lista) # Cantidad de elementos de la lista
    for i in lista: # Por cada elemento de la lista
        prom += i # Se sumara con el anterior
    promedio = prom / n # A la suma total se le divide la cantidad de elementos (Operacion para hallar el promedio)
    return promedio # Regresa el promedio
    
if __name__ == "__main__":
    e = int(input("Ingrese el tamaño de la lista: ")) # Variable "e" que decide el tamaño de la lista
    lista = crearlista(e) # Se llama la funcion lista
    promedio = calcularpromedio(lista) # Se llama la funcion promedio
    print("El promedio de los elementos de: " + str(lista) + " Es: " + str(promedio)) # Se imprime el promedio de la lista
```
</p></details></br>

### 2. Desarrollar un algoritmo que calcule el producto punto de dos arreglos de números enteros (reales) de igual tamaño.

<details><summary>codigo</summary><p>

``` python
def crearlista1(e:int)->list:
    """
    Crea una lista de números flotantes.

    Args:
    e (int): Un entero que indica la cantidad de elementos que se deben ingresar en la lista.
    
    returns:
    list: Una lista de números flotantes.
    
    """
    lista1 = []
    for i in range(e):
        n = float(input("Ingrese un numero para la primera lista: "))
        lista1.append(n)
    return lista1

def crearlista2(e:int)->list:
    """
    Crea una lista de números flotantes.

    Args:
    e (int): Un entero que indica la cantidad de elementos que se deben ingresar en la lista.
    
    returns:
    list: Una lista de números flotantes.
    
    """
    lista2 = []
    for i in range(e):
        m = float(input("Ingrese un numero para la segunda lista: "))
        lista2.append(m)
    return lista2

def calcularproductopunto(lista1,lista2):
    """
    Calcula el promedio punto de dos arreglos de numeros enteros de igual tamaño

    Args:
    lista1: lista la cual se le sacara el producto punto frente a la lista2
    lista2: lista la cual se le sacara el producto punto frente a la lista1
    
    returns:
    productopunto: El producto punto de la lista1 y lista2
    
    """
    lista3 = [] # Se crea una lista vacia
    producto = 1 # Se inicializa en 1 para no afectar la multiplicacion
    productopunto = 0 # Se inicializa en 0 para no afectar la suma
    
    for i in range(e): # Se itera segun la longitud de la lista
        producto = lista1[i] * lista2[i] # Se multiplica el elemento "i" de la lista 1 y de la lista 2
        lista3.append(producto) # El producto calculado se agrega a la lista3
        
    for i in lista3: # Por cada elemento de la lista3
        productopunto += i # Se suma con el anterior hasta haberse sumado todos los elementos de la lista, siguiendo esta operacion -> (ab = [a1b1 + a2b2 + a3b3 + ...... + anbn])
    return productopunto # Regresa el producto punto de las 2 listas

if __name__ == "__main__":
    e = int(input("Ingrese el tamaño de las listas: ")) # La longitud de las dos listas (Se pide solo una vez ya que deben ser de igual tamañp)
    lista1 = crearlista1(e) # Se llama la funcion de la lista 1
    lista2 = crearlista2(e) # Se llama la funcion de la lista 2 
    producto = calcularproductopunto(lista1,lista2) # Se llama la funcion del producto punto
    # Se imprimen las listas ingresadas y el producto punto de estos dos arreglos
    print("lista 1: " + str(lista1)) 
    print("lista 2: " + str(lista2))
    print("El producto punto de las dos listas ingresadas es: " + str(producto))
```
</p></details></br>

### 3. Hacer un algoritmo que deje al final de un arreglo de números todos los ceros que aparezcan en dicho arreglo.

<details><summary>codigo</summary><p>

``` python
def crearlista(e:int)->list:
    """
    Crea una lista de números flotantes.

    Args:
    e (int): Un entero que indica la cantidad de elementos que se deben ingresar en la lista.
    
    returns:
    list: Una lista de números flotantes.
    
    """
    lista = [] #Se crea una lista vacia
    for i in range(e): #El tamaño lo decidira la variable "e"
        n = int(input("Ingrese un numero para la lista: ")) # Se le preguntara al usuario por cada elemento que ingresara
        lista.append(n) # Agrega ese elemento
    return lista # Regresa la lista

def buscarcero(lista):
    """
    Modifica una lista dejando todos los ceros que aparecen en la lista al final de esta.

    Args:
    lista: Una lista de elementos numericos ingresada por el usuario.
    
    returns:
    lista: La nueva lista modificada pero con los ceros al final de la lista
    
    """
    for i in lista: # Por cada elemento de la lista
        if i == 0: # Si en la lista se encuentra un elemento "0"
            lista.remove(i) # Se remueve el elemento 
            lista.append(i) # Y luego se agrega otra vez este elemento al final de la lista
    return lista # Se regresa la nueva lista con los ceros al final

if __name__ == "__main__":
    e = int(input("Ingrese el tamaño de las listas: ")) # Se define el tamaño de las listas
    lista = crearlista(e) # Se llama la funcion de la lista original
    print("La lista ingresadas es: " + str(lista)) # Se imrpime la lista original

    buscar = buscarcero(lista) # Se llama la funcion que modifica la lista
    print("La lista con los ceros al final es: " + str(buscar)) # Se imprime la lista modificada
```
</p></details></br>

## Gracias por leer. 
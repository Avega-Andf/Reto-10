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
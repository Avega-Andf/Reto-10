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
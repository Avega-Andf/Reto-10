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
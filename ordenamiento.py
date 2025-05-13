def insertion_sort(lista, clave=None):
    """
    Implementa el algoritmo de Insertion Sort para ordenar una lista.

    Args:
        lista (list): Lista a ordenar.
        clave (function, optional): Función para extraer la clave de comparación. 
                                    Si no se proporciona, se ordena directamente.

    Returns:
        list: Lista ordenada.
    """
    for i in range(1, len(lista)):
        elemento_actual = lista[i]
        j = i - 1

        # Comparar usando la clave si se proporciona
        while j >= 0 and (clave(lista[j]) if clave else lista[j]) > (clave(elemento_actual) if clave else elemento_actual):
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = elemento_actual

    return lista


def ordenar_nodos_alfabeticamente(nodos):
    """
    Ordena los nombres de los nodos alfabéticamente.

    Args:
        nodos (list): Lista de nombres de nodos.

    Returns:
        list: Lista de nodos ordenada alfabéticamente.
    """
    return insertion_sort(nodos)


def ordenar_rutas_por_distancia(rutas):
    """
    Ordena las rutas por distancia de menor a mayor.

    Args:
        rutas (list): Lista de rutas en formato (origen, destino, distancia).

    Returns:
        list: Lista de rutas ordenada por distancia.
    """
    return insertion_sort(rutas, clave=lambda ruta: ruta[2])


def ordenar_direcciones(direcciones):
    """
    Ordena las direcciones de puntos de interés alfabéticamente.

    Args:
        direcciones (list): Lista de direcciones.

    Returns:
        list: Lista de direcciones ordenada alfabéticamente.
    """
    return insertion_sort(direcciones)
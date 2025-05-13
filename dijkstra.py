import heapq

class Grafo:
    def __init__(self):
        self.nodos = {}
    
    def agregar_nodo(self, nombre):
        """Agrega un nodo al grafo."""
        if nombre not in self.nodos:
            self.nodos[nombre] = {}
        else:
            print(f"El nodo '{nombre}' ya existe.")
    
    def eliminar_nodo(self, nombre):
        """Elimina un nodo y todas las aristas asociadas."""
        if nombre in self.nodos:
            # Eliminar todas las aristas asociadas al nodo
            for vecino in list(self.nodos[nombre].keys()):
                del self.nodos[vecino][nombre]
            # Eliminar el nodo
            del self.nodos[nombre]
        else:
            print(f"El nodo '{nombre}' no existe.")
    
    def modificar_nodo(self, nombre_actual, nuevo_nombre):
        """Modifica el nombre de un nodo."""
        if nombre_actual in self.nodos and nuevo_nombre not in self.nodos:
            # Renombrar el nodo
            self.nodos[nuevo_nombre] = self.nodos.pop(nombre_actual)
            # Actualizar las aristas que apuntan al nodo
            for vecino in self.nodos:
                if nombre_actual in self.nodos[vecino]:
                    self.nodos[vecino][nuevo_nombre] = self.nodos[vecino].pop(nombre_actual)
        else:
            print(f"No se puede modificar el nodo '{nombre_actual}' a '{nuevo_nombre}'.")
    
    def agregar_arista(self, origen, destino, distancia):
        """Agrega una arista entre dos nodos existentes."""
        if origen in self.nodos and destino in self.nodos:
            self.nodos[origen][destino] = distancia
            self.nodos[destino][origen] = distancia  # Si el grafo es no dirigido
        else:
            print(f"Uno o ambos nodos '{origen}' y '{destino}' no existen.")
    
    def eliminar_arista(self, origen, destino):
        """Elimina una arista entre dos nodos."""
        if origen in self.nodos and destino in self.nodos[origen]:
            del self.nodos[origen][destino]
            del self.nodos[destino][origen]
        else:
            print(f"La arista entre '{origen}' y '{destino}' no existe.")
    
    def modificar_arista(self, origen, destino, nueva_distancia):
        """Modifica la distancia de una arista existente."""
        if origen in self.nodos and destino in self.nodos[origen]:
            self.nodos[origen][destino] = nueva_distancia
            self.nodos[destino][origen] = nueva_distancia  # Si el grafo es no dirigido
        else:
            print(f"La arista entre '{origen}' y '{destino}' no existe.")
    
    def obtener_nodos(self):
        """Devuelve una lista de todos los nodos en el grafo."""
        return list(self.nodos.keys())
    
    def obtener_aristas(self):
        """Devuelve una lista de todas las aristas en el grafo."""
        aristas = []
        for origen, destinos in self.nodos.items():
            for destino, distancia in destinos.items():
                aristas.append((origen, destino, distancia))
        return aristas


def encontrar_camino_mas_corto(grafo, inicio, fin):
    """
    Implementa el algoritmo de Dijkstra para encontrar la ruta más corta en un grafo.

    Args:
        grafo (Grafo): El grafo representado como un objeto de la clase Grafo.
        inicio (str): Nodo de inicio.
        fin (str): Nodo de destino.

    Returns:
        tuple: Una tupla que contiene la ruta más corta como lista de nodos y la distancia total.
    """
    # Cola de prioridad para explorar los nodos
    cola_prioridad = []
    heapq.heappush(cola_prioridad, (0, inicio))  # (distancia acumulada, nodo actual)

    # Diccionario para almacenar las distancias mínimas desde el nodo de inicio
    distancias = {nodo: float('inf') for nodo in grafo.obtener_nodos()}
    distancias[inicio] = 0

    # Diccionario para rastrear el camino más corto
    caminos = {inicio: None}

    while cola_prioridad:
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)

        # Si llegamos al nodo de destino, reconstruimos el camino
        if nodo_actual == fin:
            return reconstruir_camino(caminos, inicio, fin), distancias[fin]

        # Explorar los vecinos del nodo actual
        for vecino, distancia in grafo.nodos[nodo_actual].items():
            nueva_distancia = distancia_actual + distancia
            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                caminos[vecino] = nodo_actual
                heapq.heappush(cola_prioridad, (nueva_distancia, vecino))

    # Si no hay camino entre inicio y fin
    return None, float('inf')


def reconstruir_camino(caminos, inicio, fin):
    """
    Reconstruye el camino desde el nodo de inicio hasta el nodo de destino.

    Args:
        caminos (dict): Diccionario que contiene el nodo anterior para cada nodo.
        inicio (str): Nodo de inicio.
        fin (str): Nodo de destino.

    Returns:
        list: Lista de nodos que forman el camino en orden.
    """
    camino = []
    nodo_actual = fin
    while nodo_actual is not None:
        camino.append(nodo_actual)
        nodo_actual = caminos[nodo_actual]
    return camino[::-1]  # Invertimos el camino para que sea de inicio a fin


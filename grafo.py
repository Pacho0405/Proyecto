import json

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
            raise ValueError(f"Uno o ambos nodos '{origen}' y '{destino}' no existen.")
    
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

    def guardar_en_archivo(self, archivo):
        """Guarda el grafo en un archivo JSON."""
        try:
            with open(archivo, 'w') as f:
                json.dump(self.nodos, f, indent=4)
            print(f"Grafo guardado en '{archivo}'.")
        except Exception as e:
            print(f"Error al guardar el grafo: {e}")

    def cargar_desde_archivo(self, archivo):
        """Carga el grafo desde un archivo JSON."""
        try:
            with open(archivo, 'r') as f:
                self.nodos = json.load(f)
            print(f"Grafo cargado desde '{archivo}'.")
        except Exception as e:
            print(f"Error al cargar el grafo: {e}")
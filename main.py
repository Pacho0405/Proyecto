from grafo import Grafo

def main():
    # Inicializar el grafo de la ciudad
    ciudad_grafo = Grafo()

    # Ejemplo de agregar nodos
    ciudad_grafo.agregar_nodo("Intersección A")
    ciudad_grafo.agregar_nodo("Intersección B")
    ciudad_grafo.agregar_nodo("Intersección C")

    # Ejemplo de agregar aristas
    ciudad_grafo.agregar_arista("Intersección A", "Intersección B", 5)
    ciudad_grafo.agregar_arista("Intersección B", "Intersección C", 10)
    ciudad_grafo.agregar_arista("Intersección A", "Intersección C", 15)

    # Mostrar nodos y aristas
    print("Nodos en el grafo:", ciudad_grafo.obtener_nodos())
    print("Aristas en el grafo:", ciudad_grafo.obtener_aristas())

if __name__ == "__main__":
    main()
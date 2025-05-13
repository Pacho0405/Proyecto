import tkinter as tk
from tkinter import ttk, messagebox
import networkx as nx
import matplotlib.pyplot as plt
from ordenamiento import ordenar_nodos_alfabeticamente, ordenar_rutas_por_distancia
from dijkstra import encontrar_camino_mas_corto
from grafo import Grafo

class VentanaPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Grafos")
        self.root.geometry("800x600")  
        self.root.resizable(False, False) 


        self.root.configure(bg="#d9e6f2")  

        self.grafo = Grafo()

        # Contenedor principal centrado
        self.frame = ttk.Frame(self.root, padding=20)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        # Etiquetas y campos para ingresar nodos
        self.label_nodo = ttk.Label(self.frame, text="Nodo:", background="#d9e6f2")
        self.label_nodo.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.entry_nodo = ttk.Entry(self.frame)
        self.entry_nodo.insert(0, "A")  
        self.entry_nodo.grid(row=0, column=1, padx=10, pady=10)

        self.boton_agregar_nodo = ttk.Button(self.frame, text="Agregar Nodo", command=self.agregar_nodo)
        self.boton_agregar_nodo.grid(row=0, column=2, padx=10, pady=10)

        # Etiquetas y campos para ingresar aristas
        self.label_origen = ttk.Label(self.frame, text="Origen:", background="#d9e6f2")
        self.label_origen.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.entry_origen = ttk.Entry(self.frame)
        self.entry_origen.insert(0, "A")  
        self.entry_origen.grid(row=1, column=1, padx=10, pady=10)

        self.label_destino = ttk.Label(self.frame, text="Destino:", background="#d9e6f2")
        self.label_destino.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.entry_destino = ttk.Entry(self.frame)
        self.entry_destino.insert(0, "B")  
        self.entry_destino.grid(row=2, column=1, padx=10, pady=10)

        self.label_peso = ttk.Label(self.frame, text="Peso:", background="#d9e6f2")
        self.label_peso.grid(row=3, column=0, padx=10, pady=10, sticky="e")
        self.entry_peso = ttk.Entry(self.frame)
        self.entry_peso.insert(0, "5.0")  
        self.entry_peso.grid(row=3, column=1, padx=10, pady=10)

        self.boton_agregar_arista = ttk.Button(self.frame, text="Agregar Arista", command=self.agregar_arista)
        self.boton_agregar_arista.grid(row=3, column=2, padx=10, pady=10)

        # Botones para editar y eliminar
        self.boton_editar_arista = ttk.Button(self.frame, text="Editar Arista", command=self.editar_arista)
        self.boton_editar_arista.grid(row=4, column=0, padx=10, pady=10)

        self.boton_eliminar_arista = ttk.Button(self.frame, text="Eliminar Arista", command=self.eliminar_arista)
        self.boton_eliminar_arista.grid(row=4, column=1, padx=10, pady=10)

        self.boton_eliminar_nodo = ttk.Button(self.frame, text="Eliminar Nodo", command=self.eliminar_nodo)
        self.boton_eliminar_nodo.grid(row=4, column=2, padx=10, pady=10)

        # Botón para calcular la ruta más corta
        self.label_inicio = ttk.Label(self.frame, text="Inicio:", background="#d9e6f2")
        self.label_inicio.grid(row=5, column=0, padx=10, pady=10, sticky="e")
        self.entry_inicio = ttk.Entry(self.frame)
        self.entry_inicio.insert(0, "A") 
        self.entry_inicio.grid(row=5, column=1, padx=10, pady=10)

        self.label_fin = ttk.Label(self.frame, text="Fin:", background="#d9e6f2")
        self.label_fin.grid(row=6, column=0, padx=10, pady=10, sticky="e")
        self.entry_fin = ttk.Entry(self.frame)
        self.entry_fin.insert(0, "B")  
        self.entry_fin.grid(row=6, column=1, padx=10, pady=10)

        self.boton_calcular_ruta = ttk.Button(self.frame, text="Calcular Ruta Más Corta", command=self.calcular_ruta)
        self.boton_calcular_ruta.grid(row=6, column=2, padx=10, pady=10)

        # Botón para mostrar el grafo visualmente
        self.boton_ver_mapa = ttk.Button(self.frame, text="Ver Mapa", command=self.mostrar_grafo_visual)
        self.boton_ver_mapa.grid(row=7, column=1, padx=10, pady=10)

    def agregar_nodo(self):
        nodo = self.entry_nodo.get()
        if nodo:
            self.grafo.agregar_nodo(nodo)
            messagebox.showinfo("Éxito", f"Nodo '{nodo}' agregado.")
            self.entry_nodo.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Debe ingresar un nombre para el nodo.")

    def agregar_arista(self):
        origen = self.entry_origen.get()
        destino = self.entry_destino.get()
        try:
            peso = float(self.entry_peso.get())
            self.grafo.agregar_arista(origen, destino, peso)
            messagebox.showinfo("Éxito", f"Arista de '{origen}' a '{destino}' con peso {peso} agregada.")
            self.entry_origen.delete(0, tk.END)
            self.entry_destino.delete(0, tk.END)
            self.entry_peso.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Debe ingresar un peso válido.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def editar_arista(self):
        origen = self.entry_origen.get()
        destino = self.entry_destino.get()
        try:
            nuevo_peso = float(self.entry_peso.get())
            self.grafo.modificar_arista(origen, destino, nuevo_peso)
            messagebox.showinfo("Éxito", f"Arista de '{origen}' a '{destino}' actualizada con peso {nuevo_peso}.")
        except ValueError:
            messagebox.showerror("Error", "Debe ingresar un peso válido.")
        except KeyError:
            messagebox.showerror("Error", "La arista especificada no existe.")

    def eliminar_arista(self):
        origen = self.entry_origen.get()
        destino = self.entry_destino.get()
        if origen and destino:
            self.grafo.eliminar_arista(origen, destino)
            messagebox.showinfo("Éxito", f"Arista de '{origen}' a '{destino}' eliminada.")
        else:
            messagebox.showerror("Error", "Debe ingresar los nodos de origen y destino.")

    def eliminar_nodo(self):
        nodo = self.entry_nodo.get()
        if nodo:
            self.grafo.eliminar_nodo(nodo)
            messagebox.showinfo("Éxito", f"Nodo '{nodo}' eliminado.")
        else:
            messagebox.showerror("Error", "Debe ingresar el nombre del nodo.")

    def calcular_ruta(self):
        inicio = self.entry_inicio.get()
        fin = self.entry_fin.get()
        if inicio and fin:
            camino, distancia = encontrar_camino_mas_corto(self.grafo, inicio, fin)
            if camino:
                messagebox.showinfo("Ruta Más Corta", f"Camino: {' -> '.join(camino)}\nDistancia: {distancia}")
            else:
                messagebox.showerror("Error", "No se encontró un camino entre los nodos.")
        else:
            messagebox.showerror("Error", "Debe ingresar los nodos de inicio y fin.")

    def mostrar_grafo_visual(self):
        """Muestra el grafo visualmente usando networkx y matplotlib."""
        G = nx.Graph()

        # Agregar nodos y aristas al grafo de networkx
        for nodo in self.grafo.obtener_nodos():
            G.add_node(nodo)

        for origen, destino, peso in self.grafo.obtener_aristas():
            G.add_edge(origen, destino, weight=peso)

        # Dibujar el grafo
        pos = nx.spring_layout(G)  # Layout para posicionar los nodos
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_weight='bold')
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=8)

        # Mostrar el grafo
        plt.title("Mapa del Grafo")
        plt.show()


if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaPrincipal(root)
    root.mainloop()
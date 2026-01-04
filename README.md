# Pacman IA

Proyecto de prácticas de la asignatura **Inteligencia Artificial**
del Grado en Ingeniería Informática.

El proyecto utiliza el entorno **Pacman AI** desarrollado por la
Universidad de Berkeley como framework base para la implementación
de distintos agentes y algoritmos de búsqueda.

---

## Contenido del repositorio

El repositorio está organizado por bloques de la asignatura:

- **SearchAlgorithms/**  
  Implementación de algoritmos de búsqueda:
  - Agente de exploración
  - Depth-First Search (DFS)
  - A* Search

- **GameTheory/**  
  (Pendiente) Implementación de agentes de teoría de juegos
  como Minimax, Alpha-Beta y Expectimax.

---

## Parte 1 – Algoritmos de Búsqueda

En la carpeta `SearchAlgorithms` se encuentra el trabajo correspondiente
a la primera parte de la práctica.

### Algoritmos implementados

- **ExplorationAgent**  
  Agente propio orientado a la exploración del entorno, priorizando
  casillas no visitadas y reduciendo repeticiones.

- **Depth-First Search (DFS)**  
  Algoritmo de búsqueda no informada basado en una estructura LIFO (pila).

- **A\***  
  Algoritmo de búsqueda informada que combina el coste acumulado del
  camino y una función heurística.

El código principal modificado se encuentra en:
- `search.py`
- `searchAgents.py`

---

## Ejecución

Ejemplo de ejecución del agente de exploración:
_Los siguientes comandos deben ejecutarse desde la carpeta `SearchAlgorithms`._

```bash
python pacman.py --pacman ExplorationAgent -k 0 
```

Ejemplo de ejecución de DFS:

```bash
python pacman.py -l mediumMaze -p SearchAgent -a fn=depthFirstSearch -k 0
```

Ejemplo de ejecución de A*:

```bash
python pacman.py -l mediumMaze -p SearchAgent -a fn=aStarSearch -k 0
```
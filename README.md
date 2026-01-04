![img.png](img.png)
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
  Búsqueda en juegos multiagente:
  - Minimax
  - Alpha-Beta Pruning
  - Expectimax
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
## Parte 2 – Teoría de Juegos

En la carpeta `GameTheory` se encuentra el trabajo correspondiente
a la segunda parte de la práctica.

### Algoritmos implementados

**Minimax**  
Algoritmo de toma de decisiones en entornos multiagente que asume
oponentes racionales. Pacman actúa como agente maximizador y los
fantasmas como agentes minimizadores.

**Alpha-Beta Pruning**  
Optimización del algoritmo Minimax que reduce el número de nodos
explorados mediante poda alfa-beta, manteniendo el mismo resultado
final.

**Expectimax**  
Variante de Minimax que modela el comportamiento de los fantasmas
como aleatorio, calculando valores esperados en lugar de mínimos.

El código principal modificado se encuentra en:
- `submission.py`

---

## Ejecución

_Los siguientes comandos deben ejecutarse desde la carpeta `SearchAlgorithms`._

Ejemplo de ejecución del agente de exploración:

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
_Los siguientes comandos deben ejecutarse desde la carpeta `GameTheory`._

Ejemplo de ejecución del agente Minimax:

```bash
python pacman.py -p MinimaxAgent -l minimaxClassic -a depth=3 -k 1
```

Ejemplo de ejecución del agente Alpha-Beta:

```bash
python pacman.py -p AlphaBetaAgent -l minimaxClassic -a depth=3 -k 1
```

Ejemplo de ejecución del agente Expectimax:

```bash
python pacman.py -p ExpectimaxAgent -l trappedClassic -a depth=3 -k 1

```
## Escenarios disponibles

Los siguientes escenarios están disponibles para probar los agentes:

### Parte 1 – Algoritmos de Búsqueda
- `smallMaze`
- `mediumMaze`
- `bigMaze`
- `bigSafeSearch`
- `originalClassic`
- `powerClassic` 
- `trickySearch`
- `greedySearch`
- `openMaze`
- `openClassic`
- `openSearch`

### Parte 2 – Teoría de Juegos
- `capsuleClassic`
- `contestClassic`
- `minimaxClassic`
- `openClassic`
- `originalClassic`
- `smallClassic`
- `testClassic`
- `trappedClassic`
- `trickyClassic`

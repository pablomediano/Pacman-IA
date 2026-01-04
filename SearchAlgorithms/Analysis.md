# Tabla de análisis búsqueda DEFAULT

| Laberinto       | Coste acumulado  (Score) | Total de pasos | Número de casillas exploradas | Ratio de repetición (%) |
|-----------------|:------------------------:|:--------------:|:-----------------------------:|:-----------------------:|
| smallMaze       |           414            |       96       |              57               |          0.41           |
| mediumMaze      |           345            |      165       |              135              |          0.18           |
| bigMaze         |           -391           |      901       |              467              |          0.48           |
| bigSafeSearch   |           385            |      125       |              101              |          0.59           |
| originalClassic |           382            |      225       |              157              |          0.41           |
| powerClassic    |           ***            |      ***       |              ***              |           ***           |
| trickySearch    |           447            |       63       |              51               |          0.19           |
| greedySearch    |           494            |       16       |               9               |          0.44           |
| openMaze        |           -918           |      1428      |              614              |          0.43           |
| openClassic     |           387            |      123       |              98               |          0.20           |
| openSearch      |           402            |      108       |              68               |          0.37           |


# Tabla de análisis búsqueda no informada DFS e informada *A *SIN FANTASMAS*

| Laberinto       | Agente | Tiempo de ejecución (s) | Coste acumulado | Total de pasos | Número de casillas exploradas | Eficiencia estimada (%) | Nodos expandidos | ¿Completó objetivo? |
|-----------------|:------:|:-----------------------:|:---------------:|:--------------:|:-----------------------------:|:-----------------------:|:----------------:|:-------------------:|
| smallMaze       |  DFS   |          0.001          |       28        |       28       |              38               |          73.68          |        38        |          ✅          |
| smallMaze       |  *A   |          0.001          |       16        |       16       |              26               |          61.54          |        26        |          ✅          |
| mediumMaze      |  DFS   |          0.004          |       111       |      111       |              223              |          49.55          |       224        |          ✅          |
| mediumMaze      |  *A   |          0.002          |       39        |       39       |              64               |          60.94          |        64        |          ✅          |
| bigMaze         |  DFS   |          0.007          |       188       |      188       |              428              |          43.93          |       428        |          ✅          |
| bigMaze         |  *A   |          0.009          |       188       |      188       |              497              |          37.83          |       497        |          ✅          |
| bigSafeSearch   |  DFS   |          0.001          |       23        |       23       |              28               |          82.14          |        28        |          ✅          |
| bigSafeSearch   |  *A   |          0.001          |       19        |       19       |              43               |          44.19          |        43        |          ✅          |
| originalClassic |  DFS   |          0.004          |       141       |      141       |              211              |          66.82          |       211        |          ✅          |
| originalClassic |  *A   |          0.002          |       37        |       37       |              75               |          49.33          |        75        |          ✅          |
| powerClassic    |  DFS   |           ***           |       ***       |      ***       |              ***              |           ***           |       ***        |         ***         |
| powerClassic    |  *A   |           ***           |       ***       |      ***       |              ***              |           ***           |       ***        |         xxx         |
| trickySearch    |  DFS   |          0.002          |       52        |       52       |              57               |          91.23          |        57        |          ✅          |
| trickySearch    |  *A   |          0.002          |       32        |       32       |              59               |          52.46          |        61        |          ✅          |
| greedySearch    |  DFS   |          0.001          |        4        |       4        |               9               |          44.44          |        9         |          ✅          |
| greedySearch    |  *A   |          0.001          |        4        |       4        |               4               |           100           |        4         |          ✅          |
| openMaze        |  DFS   |          0.010          |       262       |      262       |              666              |          26.63          |       984        |          ✅          |
| openMaze        |  *A   |          0.007          |       44        |       44       |              389              |          11.31          |       389        |          ✅          |
| openClassic     |  DFS   |          0.03           |       109       |      109       |              109              |           100           |       109        |          ✅          |
| openClassic   |  *A   |          0.002          |       15        |       15       |              65               |          23.08          |        65        |        ✅         |
| openSearch   |  DFS   |          0.001          |       28        |       28       |              28               |           100           |        28        |          ✅          |
| openSearch   |  *A  |          0.001          |       10        |       10       |              26               |          38.46          |        26        |         ✅         |
# Tabla de análisis búsqueda no informada DFS e informada *A *CON FANTASMAS*

| Laberinto       | Agente | Tiempo de ejecución (s) | Coste acumulado | Total de pasos | Número de casillas exploradas | Eficiencia estimada (%) | Nodos expandidos | ¿Completó objetivo? | ¿Fue atrapado? |
|-----------------|:------:|:-----------------------:|:---------------:|:--------------:|:-----------------------------:|:-----------------------:|:----------------:|:-------------------:|:--------------:|
| smallMaze       |  DFS   |          0.001          |       28        |       28       |              38               |          73.68          |        38        |          ✅          |       ❌        |
| smallMaze       |  *A    |          0.001          |       16        |       16       |              26               |          61.54          |        26        |          ✅          |       ❌        |
| mediumMaze      |  DFS   |          0.004          |       111       |      111       |              223              |          49.55          |       224        |          ✅          |       ❌        |
| mediumMaze      |  *A    |          0.002          |       39        |       39       |              64               |          60.94          |        64        |          ✅          |       ❌        |
| bigMaze         |  DFS   |          0.007          |       188       |      188       |              428              |          43.93          |       428        |          ✅          |       ❌        |
| bigMaze         |  *A    |          0.009          |       188       |      188       |              497              |          37.83          |       497        |          ✅          |       ❌        |
| bigSafeSearch   |  DFS   |          0.001          |       23        |       23       |              28               |          82.14          |        28        |          ✅          |       ❌        |
| bigSafeSearch   |  *A    |          0.001          |       19        |       19       |              43               |          44.19          |        43        |          ✅          |       ❌        |
| originalClassic |  DFS   |          0.008          |       141       |      141       |              211              |          66.82          |       211        |          ❌          |       ✅        |
| originalClassic |  *A    |          0.005          |       37        |       37       |              75               |          49.33          |        75        |          ✅          |       ❌        |
| powerClassic    |  DFS   |           ***           |       ***       |      ***       |              ***              |           ***           |       ***        |         ***         |      ***       |
| powerClassic    |  *A    |           ***           |       ***       |      ***       |              ***              |           ***           |       ***        |         ***         |      ***       |
| trickySearch    |  DFS   |          0.002          |       52        |       52       |              57               |          91.23          |        57        |          ✅          |       ❌        |
| trickySearch    |  *A    |          0.002          |       32        |       32       |              59               |          52.46          |        61        |          ✅          |       ❌        |
| greedySearch    |  DFS   |          0.001          |        4        |       4        |               9               |          44.44          |        9         |          ✅          |       ❌        |
| greedySearch    |  *A    |          0.001          |        4        |       4        |               4               |           100           |        4         |          ✅          |       ❌        |
| openMaze        |  DFS   |          0.010          |       262       |      262       |              666              |          26.63          |       984        |          ✅          |       ❌        |
| openMaze        |  *A    |          0.007          |       44        |       44       |              389              |          11.31          |       389        |          ✅          |       ❌        |
| openClassic     |  DFS   |          0.005          |       109       |      109       |              109              |           100           |       109        |            ✅         |       ❌          |
| openClassic     |  *A    |          0.005          |       15        |       15       |              65               |          23.08          |        65        |             ✅        |        ❌        |
| openSearch      |  DFS   |          0.001          |       28        |       28       |              28               |           100           |        28        |          ✅          |       ❌        |
| openSearch      |  *A    |          0.001          |       10        |       10       |              26               |          38.46          |        26        |          ✅          |       ❌        |

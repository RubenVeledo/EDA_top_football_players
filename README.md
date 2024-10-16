![imagen](https://static0.givemesportimages.com/wordpress/wp-content/uploads/2024/05/toni-kroos-2.jpg)
<h1 align="center">🏆 Bajo el radar: buscando al nuevo maestro del mediocampo del Real Madrid 🏆 </h1>

### 📋 Descripción del proyecto 📋

En la era del big data, el análisis de datos en el deporte se ha vuelto esencial para mejorar el rendimiento y la toma de decisiones. Este proyecto se dedica a realizar un análisis exploratorio de datos (EDA) sobre jugadores de fútbol en las cinco grandes ligas europeas. La investigación se centra en la búsqueda de un sustituto para Toni Kroos, utilizando métricas de rendimiento y visualizaciones que permitan un entendimiento profundo del impacto que tiene un mediocentro en su equipo. A través de un enfoque detallado y analítico, este proyecto aspira a aportar información valiosa para la toma de decisiones estratégicas.

-------------------------

### 🎯 **Objetivo del Proyecto** 🎯

Este proyecto tiene como objetivo **identificar a un sustituto válido** para el destacado mediocampista **Toni Kroos**, aprovechando un análisis de datos de jugadores de las **cinco grandes ligas europeas**:

- LaLiga
- Premier League
- Bundesliga
- Serie A
- Ligue 1

### 📊 **Metodología:** 📊

A través de un **análisis exploratorio de datos (EDA)**, se evaluarán métricas clave como:

**Métricas de aporte ofensivo**:
- Goles.
- Asistencias.
- Asistencias esperadas.

**Métricas de control de juego:**
- Pases progresivos.
- Asistencias progresivas.

**Métrica de participación:**
- Minutos jugados.

-------------------------------------------------

### Descripción de las columnas del dataframe

| **Variable**              | **Definición eng/esp**                                                                                   |
|---------------------------|--------------------------------------------------------------------------------------------------|
| **Player**                | The name of the player. <br> El nombre del jugador.                                           |
| **Nation**                | The player's nationality. <br> La nacionalidad del jugador.                                    |
| **Pos**                   | The player's position (e.g., forward, midfielder, defender). <br> La posición del jugador (por ejemplo, delantero, centrocampista, defensor). |
| **Age**                   | The player's age. <br> La edad del jugador.                                                   |
| **MP (matches played)**   | Total matches played number. <br> Número total de partidos jugados.                          |
| **Starts**                | Number of matches the player started. <br> Número de partidos en los que el jugador fue titular. |
| **Min (Minutes)**         | Total minutes played by the player (this might be the same as MP). <br> Total de minutos jugados por el jugador (esto podría ser lo mismo que MP). |
| **90s (90s Played)**     | The equivalent of 90-minute matches played by the player (e.g., 1.5 = 135 minutes). <br> El equivalente de partidos de 90 minutos jugados por el jugador (por ejemplo, 1.5 = 135 minutos). |
| **Gls (Goals)**           | Total number of goals scored by the player. <br> Número total de goles anotados por el jugador. |
| **Ast (Assists)**         | Total number of assists made by the player. <br> Número total de asistencias realizadas por el jugador. |
| **G+A (Goals + Assists)** | Total number of goals and assists combined. <br> Número total de goles y asistencias combinados. |
| **G-PK (Goals - Penalty Kicks)** | Total number of goals scored excluding penalty kicks. <br> Número total de goles anotados excluyendo los penales. |
| **PK (Penalty Kicks)**    | Number of penalty goals scored by the player. <br> Número de goles de penalti anotados por el jugador. |
| **PKatt (Penalty Kicks Attempted)** | Number of penalty kicks attempted by the player. <br> Número de penales intentados por el jugador. |
| **CrdY (Yellow Cards)**   | Number of yellow cards received by the player. <br> Número de tarjetas amarillas recibidas por el jugador. |
| **CrdR (Red Cards)**      | Number of red cards received by the player. <br> Número de tarjetas rojas recibidas por el jugador. |
| **xG (Expected Goals)**   | The expected number of goals from the player's shots. <br> El número esperado de goles de los disparos del jugador. |
| **npxG (Non-Penalty Expected Goals)** | Expected goals excluding penalties. <br> Goles esperados excluyendo los penales. |
| **xAG (Expected Assists)** | The expected number of assists from the player's passes. <br> El número esperado de asistencias de los pases del jugador. |
| **npxG+xAG (Non-Penalty xG + xAG)** | Total of non-penalty expected goals and expected assists. <br> Total de goles esperados no penales y asistencias esperadas. |
| **PrgC (Progressive Carries)** | Number of times the player carried the ball forward. <br> Número de veces que el jugador llevó el balón hacia adelante. |
| **PrgP (Progressive Passes)** | Number of passes made by the player that moved the ball forward. <br> Número de pases realizados por el jugador que movieron el balón hacia adelante. |
| **PrgR (Progressive Runs)** | Number of times the player made runs forward with the ball. <br> Número de veces que el jugador hizo carreras hacia adelante con el balón. |
| **G+A-PK (Goals + Assists - Penalty Kicks)** | Total goals and assists minus penalty goals. <br> Número total de goles y asistencias menos los goles de penalti. |
| **xG+xAG (Expected Goals + Expected Assists)** | Total expected goals and assists. <br> Total de goles y asistencias esperados. |

----------------------------

### 🎁 Una pequeña muestra 🎁

![Muestra](.data\src\notebooks\Wirtz vs Kroos.png)

--------------------------------

### 🛠️ Construido con 🛠️

[![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/Numpy-013243?style=flat-square&logo=numpy&logoColor=white)](https://numpy.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-003b57?style=flat-square&logo=matplotlib&logoColor=white)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-9A1B30?style=flat-square&logo=seaborn&logoColor=white)](https://seaborn.pydata.org/)

-------------------------------------

### ✒️ Autor ✒️

- Rubén Veledo.

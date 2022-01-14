#Con este código se crean seis gráficas con las estadisticas de de un equipo pokemon al estilo del propio juego

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pokemons = ["Honchrow", "Torterra", "Drapion", "Bastiodon", "Gallade", "Gastrodon"]
stats = ["HP", "Ataque", "Defensa", "At.Esp", "Def.Esp", "Velocidad"]


honchrow=[280,244,130,192,113,139]
torterra=[217,201,167,136,127,100]
drapion=[180,152,172,105,105,148]
bastiodon=[200,121,285,110,222,86]
gallade=[175,198,88,101,164,134]
gastrodon=[156,148,123,162,150,78]


plt.figure(figsize=(20,12))
theta = np.linspace (0,2 * np.pi, len (stats), endpoint = False) #Con theta se establecen la colocación de los puntos en los grados de la circunferencia, que los puntos sean
                                                                 #la longitud de la variable stats y que no haya un punto final para que este relleno


ax = plt.subplot (231, projection = 'polar') #De esta manera se crea el gáfico circular
ax.plot (theta, honchrow, 'r-', lw = 1, alpha = 0.75) #Se crean los puntos dentro del grafico con las estadisticas de la lista honchrow
ax.fill (theta, honchrow, 'r', alpha = 0.75) #La misma mecanica que arriba pero en vez de puntos es un relleno 
ax.set_thetagrids (theta * 180 / np.pi, stats) #Se establecen los nombres de los campos
ax.set_ylim (0,300) #Se establece el rango en el que pueden ir los datos de la gráfica
ax.set_theta_zero_location ('N') #Se orienta la grafica hacia el norte y así el primer dato aparece en 90º
ax.set_title ('Honchrow') #Titulo de la gáfica

ax = plt.subplot (232, projection = 'polar')
ax.plot (theta, torterra, 'r-', lw = 1, alpha = 0.75)
ax.fill (theta, torterra, 'r', alpha = 0.75)
ax.set_thetagrids (theta * 180 / np.pi, stats)
ax.set_ylim (0,300)
ax.set_theta_zero_location ('N')
ax.set_title ('Torterra')

ax = plt.subplot (233, projection = 'polar')
ax.plot (theta, drapion, 'r-', lw = 1, alpha = 0.75)
ax.fill (theta, drapion, 'r', alpha = 0.75)
ax.set_thetagrids (theta * 180 / np.pi, stats)
ax.set_ylim (0,300)
ax.set_theta_zero_location ('N')
ax.set_title ('Drapion')

ax = plt.subplot (234, projection = 'polar')
ax.plot (theta, bastiodon, 'r-', lw = 1, alpha = 0.75)
ax.fill (theta, bastiodon, 'r', alpha = 0.75)
ax.set_thetagrids (theta * 180 / np.pi, stats)
ax.set_ylim (0,300)
ax.set_theta_zero_location ('N')
ax.set_title ('Bastiodon')

ax = plt.subplot (235, projection = 'polar')
ax.plot (theta, gallade, 'r-', lw = 1, alpha = 0.75)
ax.fill (theta, gallade, 'r', alpha = 0.75)
ax.set_thetagrids (theta * 180 / np.pi, stats)
ax.set_ylim (0,300)
ax.set_theta_zero_location ('N')
ax.set_title ('Gallade')

ax = plt.subplot (236, projection = 'polar')
ax.plot (theta, gastrodon, 'r-', lw = 1, alpha = 0.75)
ax.fill (theta, gastrodon, 'r', alpha = 0.75)
ax.set_thetagrids (theta * 180 / np.pi, stats)
ax.set_ylim (0,300)
ax.set_theta_zero_location ('N')
ax.set_title ('Gastrodon')

plt.show()

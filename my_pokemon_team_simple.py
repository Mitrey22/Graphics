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

plt.figure(figsize=(20,8))

plt.subplot(2,3,1)
plt.grid(True)
plt.bar(stats, honchrow)
plt.title("Honchrow")

plt.subplot(2,3,2)
plt.grid(True)
plt.bar(stats, torterra)
plt.title("Torterra")

plt.subplot(2,3,3)
plt.grid(True)
plt.bar(stats, drapion)
plt.title("Drapion")

plt.subplot(2,3,4)
plt.grid(True)
plt.bar(stats, bastiodon)
plt.title("Bastiodon")

plt.subplot(2,3,5)
plt.grid(True)
plt.bar(stats, gallade)
plt.title("Gallade")

plt.subplot(2,3,6)
plt.grid(True)
plt.bar(stats, gastrodon)
plt.title("Gastrodon")


plt.show()

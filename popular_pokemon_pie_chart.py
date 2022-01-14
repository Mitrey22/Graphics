import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

y = ["Umbreon", "Charizard", "Mimikyu", "Lucario", "Greninja"]
x = [67062, 93968, 99077, 102259, 140559]

plt.title("Pokemon of the year 2020 (voted by people)")
plt.pie(x, labels = y,
        startangle = 90,
        colors = ["grey", "orange", "yellow", "#5478E3", "#000EFF"],
        radius = 1.2,
        autopct="%1.2f%%")

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({"x": ["MT1", "MT2", "MT5", "MT8", "MT10", "MT15", "MT16", "MT18", "MT22", "MT23",
                         "MT25", "MT30", "MT31", "MT34", "MT36", "MT40", "MT43", "MT46", "MT49", "MT50"],
                   "y": [48, 18, 46, 103, 143, 77, 18, 47, 38, 12,
                         51, 33, 151, 151, 20, 102, 12, 34, 21, 151]})


plt.hist(df.y, bins=5,histtype="bar", rwidth=0.75)
plt.grid(True)
plt.xlabel("Nº pokemon")
plt.ylabel("Frecuencia")
plt.title("Cantidad de pokemon que aprenden ciertos MT's 1a generación")
plt.show()

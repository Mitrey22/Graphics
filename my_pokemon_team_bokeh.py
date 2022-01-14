import pandas as pd
import numpy as np
from bokeh.models import ColumnDataSource, FactorRange
from bokeh.plotting import figure, show
from bokeh.io import output_notebook
from bokeh.transform import factor_cmap

pokemons = ["Honchrow", "Torterra", "Drapion", "Bastiodon", "Gallade", "Gastrodon"]
stats = ["Nivel", "PS", "Ataque", "Defensa", "At.Esp", "Def.Esp", "Velocidad"]
data = {'Pokemon' : pokemons,
        'Nivel': [80,67,63,72,61,68],
        'PS' : [280,217,180,200,175,156],
        'Ataque' : [244,201,152,121,198,148],
        'Defensa' : [130,167,172,285,88,123],
        'At.Esp': [192,136,105,110,101,162],
        'Def.Esp': [113,127,105,222,164,150],
        'Velocidad': [139,100,148,86,134,78]}
        
        
x = [ (pokemon, stat) for pokemon in pokemons for stat in stats ]
counts = sum(zip(data['Nivel'], data['PS'], data['Ataque'], data['Defensa'], data['At.Esp'], data['Def.Esp'], data['Velocidad']), ())

source = ColumnDataSource(data=dict(x=x, counts=counts))


p = figure(x_range=FactorRange(*x), height=250, title="Pokemon stats",
           toolbar_location=None, tools="")

output_notebook()

colors = ["white", "#39CE36", "red", "blue", "#951111", "#0F1F72", "#E4EA65"]


p.width = 3000
p.vbar(x='x', top='counts', width=0.9, source=source, 
       fill_color=factor_cmap('x', palette=colors, factors=stats, start=1, end=3))

show(p)

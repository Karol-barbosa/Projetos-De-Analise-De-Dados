# sea_level_predictor.py

import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Importar dados
    df = pd.read_csv("epa-sea-level.csv")

    # Criar gráfico de dispersão
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Primeira linha de regressão (1880 até 2050)
    slope, intercept, r_value, p_value, std_err = linregress(
        df["Year"], df["CSIRO Adjusted Sea Level"]
    )
    years_extended = pd.Series(range(1880, 2051))
    plt.plot(years_extended, intercept + slope * years_extended, 'r', label="1880-2050")

    # Segunda linha de regressão (2000 até 2050)
    df_recent = df[df["Year"] >= 2000]
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(
        df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"]
    )
    years_recent = pd.Series(range(2000, 2051))
    plt.plot(years_recent, intercept2 + slope2 * years_recent, 'green', label="2000-2050")

    # Configuração de título e rótulos
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()

    # Salvar a imagem
    plt.savefig("sea_level_plot.png")
    return plt.gca()

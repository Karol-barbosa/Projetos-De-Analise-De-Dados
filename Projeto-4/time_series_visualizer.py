import matplotlib
matplotlib.use("Agg")  # essa parte evita erro
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=["date"], index_col="date") # lê o arquivo csv e trasforma a coluna em date

df = df[
    (df["value"] >= df["value"].quantile(0.025)) &
    (df["value"] <= df["value"].quantile(0.975)) # aqui é a limpeza dos dados, calcula os quantile de 2.5% e 97.5% da coluna value. se o valor de views for muito baixo ou absurdo de alto, ele é cortado.
]

def draw_line_plot():
    fig, ax = plt.subplots(figsize=(15, 5)) # cria uma figura e define o tamanho 15 x 5
    ax.plot(df.index, df["value"], color="red", linewidth=1) # plota um gráfico de linha 
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019") #Define título e rótulos dos eixos
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    fig.savefig("line_plot.png") # Salva a figura em um arquivo line_plot.png
    return fig


def draw_bar_plot(): # faz uma cópia do DataFrame e cria coluna auxiliares 

    df_bar = df.copy()
    df_bar["year"] = df_bar.index.year # colunas
    df_bar["month"] = df_bar.index.month # colunas

    df_grouped = df_bar.groupby(["year", "month"])["value"].mean().unstack() # agrupa ano e mês

    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"] # lista para aparecer os nomes dos meses na legenda 


    fig = df_grouped.plot(kind="bar", figsize=(10, 8)).figure #Usa o Pandas .plot(kind="bar") para gerar gráfico de barras, Cada barra representa a média de um mês, agrupado por ano.
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(title="Months", labels=months)

    fig.savefig("bar_plot.png")
    return fig


def draw_box_plot(): # Faz uma cópia e reseta o índice (a coluna "date" volta como coluna normal)
    
    df_box = df.copy().reset_index()
    df_box["year"] = [d.year for d in df_box.date] # colunas auxiliares
    df_box["month"] = [d.strftime("%b") for d in df_box.date]

    fig, axes = plt.subplots(1, 2, figsize=(15, 5))

    sns.boxplot(x="year", y="value", data=df_box, ax=axes[0])
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    sns.boxplot(
        x="month", y="value", data=df_box,
        order=["Jan", "Feb", "Mar", "Apr", "May", "Jun",
               "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        ax=axes[1]
    )
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    fig.savefig("box_plot.png")
    return fig

# aqui você lê os dados, limpa os outliers, cria 3 funções e cada uma salva um gráfico diferente

# os testes pytest chega se os gráficos tem títulos, rótulos, legendas e dados certos
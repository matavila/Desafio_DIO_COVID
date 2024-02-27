# -------------- Análise de Dados ----------------
## Projeto DIO


# (1) Començando com a importação das bibliotecas a serem utilizadas
import pandas as pd
import numpy as np
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go
import re
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt
from pmdarima.arima import auto_arima

# (2) Importando os dados a serem utilizados
Dataframe = pd.read_csv("Projetos\covid_19_data.csv")
print(Dataframe)

# (3) Formatando informações do bancos de dados 
print(Dataframe.dtypes)
#       -> Manipulações a serem feitas: Conversão dos dados da coluna ObservationDate e Last Update de string para data
            # Devido ao formato inconsistente da coluna tive que mudar o formato para mixed
Dataframe['ObservationDate'] = pd.to_datetime(Dataframe['ObservationDate'])
Dataframe['Last Update'] = pd.to_datetime(Dataframe['Last Update'])                                         


#       -> Manipulações a serem feitas: Limpeza dos nomes das colunas através da utilização da função re
def corrige_colunas(col_name):
    return re.sub(r"[/| ]","", col_name).lower()

Dataframe.columns = [corrige_colunas(col) for col in Dataframe.columns]     
print(Dataframe.dtypes)

# (4) Analisando os dados referentes ao Brasil
"""
    Para verificar a lista de paises e olhar o nome referente ao brasil usamos:
        print(Dataframe.contryregion.unique())
"""

Dataframe.loc[Dataframe.countryregion == "Brazil"]

#   -> Filtrando somente os dados a partir da primeira infecção pelo convid
Brasil = Dataframe.loc[(Dataframe.countryregion == "Brazil") & (Dataframe.confirmed > 0)]       # Duas condições para fazer a filtragem
print(Brasil)

#   -> Casos confirmados
"""
    px.line(Banco de dados, Eixo X, Eixo Y , titulo).show()  -> Para mostrar
"""
px.line(Brasil, 'observationdate', 'confirmed', title= "Casos confirmados no Brasil").show()

#   -> Verificando o quanto de casos novos há por dia
Brasil["newcases"]= list(map(
    lambda x: 0 if (x ==0 ) else Brasil["confirmed"].iloc[x] - Brasil["confirmed"].iloc[x-1],                                         # Função anonima que faz a conta da variação de casos por dia
    np.arange(Brasil.shape[0])
))
px.line(Brasil, 'observationdate', 'newcases', title= "Casos novos por dia").show()

#   -> Verificando o número de mortes por dia
Figura = go.Figure()
Figura.add_trace(
        go.Scatter(x=Brasil.observationdate, y= Brasil.deaths, name = "Mortes", mode='lines+markers',line={"color":"red"})
)
Figura.update_layout(title = "Mortes por COVID-19 no Brasil")
Figura.show()

#   -> Calculando a taxa de crescimento:

#    Para calcular temos :
#        taxa de crescimento = (presente/passado) ** (1/numero de dias) -1

def taxa_crescimento(data, variable, data_inicio = None, data_final=None): 
    # Se a primeira data for none, define como a primeira data disponivel
    if data_inicio == None:
        data_inicio = data.observationdate.loc[data[variable] >0 ].min()
    else:
        data_inicio = pd.to_datetime(data_inicio)
    
    if data_final == None:
        data_final = data.observationdate.iloc[-1]
    else:
        data_final = pd.to_datetime(data_final)

    # DEfinindo os valores da presente e passado
    passado = data.loc[data.observationdate == data_inicio, variable].values[0]
    presente = data.loc[data.observationdate == data_final, variable].values[0]

    # Definindo o número de dias
    n= (data_final - data_inicio).days

    # Calculando a taxa
    Taxa = (presente/passado)**(1/n) -1

    return Taxa*100

print(f"A taxa de crescimento total é : {round(taxa_crescimento(Brasil, 'confirmed'),2)}")


# Calculando a taxa de crescimento diário
def taxa_crescimento_diario(data, variable, data_inicio = None):
    if data_inicio == None:
        data_inicio = data.observationdate.loc[data[variable] >0 ].min()
    else:
        data_inicio = pd.to_datetime(data_inicio)
    data_final = data.observationdate.max()

    # Definindo o número de dias
    n= (data_final - data_inicio).days

    # Taxa calculada de um dia para o outro
    Taxas = list(map(
        lambda X: (data[variable].iloc[X] - data[variable].iloc[X-1]) / data[variable].iloc[X-1],
        range(1, n+1)
    ))
    return np.array(Taxas) * 100

taxa_dia = taxa_crescimento_diario(Brasil, 'confirmed')
print(taxa_dia)

# Plotando o gráfico de taxa de crescimento diário
primeiro_dia = Brasil.observationdate.loc[Brasil.confirmed > 0].min()

px.line(x = pd.date_range(primeiro_dia, Brasil.observationdate.max())[1::],y=taxa_dia ,title= "Taxa de crescimento por dia").show() 

# Predições 
"""
    Antes de começar as predições, devemos entender primeiro esta base de dados (serie) o que ela tem de tendencia, sazonalidade e ruidoas
"""

Casos_Confirmados = Brasil.confirmed
Casos_Confirmados.index = Brasil.observationdate

print(Casos_Confirmados)

Resultado = seasonal_decompose(Casos_Confirmados)
fig, (ax1,ax2,ax3,ax4) = plt.subplots(4,1, figsize = (10,8))
ax1.plot(Resultado.observed)
ax2.plot(Resultado.trend)
ax3.plot(Resultado.seasonal)
ax4.plot(Casos_Confirmados.index, Resultado.resid)
ax4.axhline(0, linestyle='dashed', c='black')
plt.show()

#Modelando pelo ARIMA (Média movel integrada autoregressiva) = modela em função do passado
Modelo= auto_arima(Casos_Confirmados)

fig = go.Figure(go.Scatter(
    x = Casos_Confirmados.index,
    y = Casos_Confirmados,
    name = 'Observados'
))

fig.add_trace(go.Scatter(
    x = Casos_Confirmados.index,
    y = Modelo.predict_in_sample(),
    name= 'Preditos'
    
    )
)

fig.add_trace(go.Scatter(
    x = pd.date_range('2020-05-20', '2020-06-20'), 
    y = Modelo.predict(31),
    name="Forecast"
    )
)

fig.update_layout(title ="Previsão de casos confirmados no Brasil para os proximos 30 dias")
fig.show()

import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from datetime import datetime
data = pd.read_csv('sat.csv')
# data.info(): informa Memória Usada, Entradas de Dados, Colunas e Tipos de Dados.
# data.head(): imprime os 5 Primeiros Registros da determinada Planilha de Dados.
timestamp = 42368.149155
dt_object = datetime.fromtimestamp(timestamp)
# Converte a variável timestamp em um tipo Datetime.
for i in data['time']:
    dt_object = datetime.fromtimestamp(i)
    print(dt_object)
# Looping que printa os Objetos Datetime de cada Elemento do Array data['time'].
data['Time_Analysis'] = pd.to_datetime(data['time'], unit='s')
# Cria uma Nova Coluna que analisa uma relação entre timestamp e time.
# Unidade 's' ajuda a converter tempo no Padrão Temporal do Meridiano de Greenwich (GMT).
data.wind_speed.isnull().sum()
data = data.dropna(how = 'any', axis = 0)
# Checa a presença de Linhas Nulas e as exclui.
data. shape
feature_col = ['X', 'Y', 'time']
# Cuida do Conjunto de Dados de Feature
target = ['wind_speed']
# Cuida do Conjunto de Dados dos Alvos (Targets)
X = data[feature_col]
y = data[target]
sns.pairplot(data, x_vars = ['X', 'Y', 'time'], y_vars = 'wind_speed')
# Estruturação de Gráfico praticamente Uniforme, de Feature, Target e Tempo.
plt.show()
# Mostra a projeção gráfica.
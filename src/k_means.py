import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

def load_data(file_path, delimiter=","):
    """
    Carrega um arquivo CSV ou outro formato delimitado em um DataFrame do pandas.

    :param file_path: Caminho do arquivo.
    :param delimiter: Delimitador dos dados (padrão é ',').
    :return: DataFrame carregado.
    """
    try:
        data = pd.read_csv(file_path, delimiter=delimiter)
        print(f"Dados carregados com sucesso de {file_path}.")
        return data
    except Exception as e:
        print(f"Erro ao carregar dados: {e}")
        return None

def plot_boxplots(df, column_name, group_by):
    """
    Plota boxplots para uma coluna específica, agrupando por outra coluna.

    :param df: DataFrame com os dados.
    :param column_name: Nome da coluna a ser plotada.
    :param group_by: Coluna para agrupar os dados (ex: 'activity').
    """
    try:
        plt.figure(figsize=(10, 6))
        sns.boxplot(x=group_by, y=column_name, data=df)
        plt.title(f"Boxplot de {column_name} agrupado por {group_by}")
        plt.show()
    except Exception as e:
        print(f"Erro ao plotar boxplots: {e}")

def normalize_features(df, columns):
    """
    Normaliza as colunas especificadas do DataFrame.

    :param df: DataFrame com os dados.
    :param columns: Lista de colunas a serem normalizadas.
    :return: DataFrame com as colunas normalizadas.
    """
    try:
        scaler = StandardScaler()
        df[columns] = scaler.fit_transform(df[columns])
        print("Colunas normalizadas com sucesso.")
        return df
    except Exception as e:
        print(f"Erro ao normalizar colunas: {e}")
        return df

def plot_time_series(df, columns, title="Séries Temporais"):
    """
    Plota séries temporais para colunas selecionadas.

    :param df: DataFrame com os dados.
    :param columns: Lista de colunas para plotar.
    :param title: Título do gráfico.
    """
    try:
        plt.figure(figsize=(12, 6))
        for col in columns:
            plt.plot(df[col], label=col)
        plt.title(title)
        plt.legend()
        plt.show()
    except Exception as e:
        print(f"Erro ao plotar séries temporais: {e}")

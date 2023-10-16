"""Esse é o módulo de extração de dados."""

import glob  # biblioteca para listar arquivos
import os  # bliblioteca para manipular arquivos e pastas
from typing import List

import pandas as pd


def ler_arquivos_excel(input_path: str) -> List[pd.DataFrame]:
    """
    Função para ler os arquivos de uma pasta data/input e retornar uma lista de dataframes.
    
    args: input_path (str): caminho da pastas com os arquivos
    return: list: Lista de dataframes
    """
    files = glob.glob(os.path.join(input_path, '*.xlsx'))

    dataframes = []
    for file in files:
        # Lê o arquivo Excel em um dataframe
        df = pd.read_excel(file)
        dataframes.append(df)

    return dataframes

if __name__ == '__main__':
    path = 'app/data/input'
    data_frame_list = ler_arquivos_excel(path)
    print(data_frame_list)

import os # bliblioteca para manipular arquivos e pastas
import glob # biblioteca para listar arquivos

import pandas as pd

from typing import List

def ler_arquivos_excel(input_path: str) -> List[pd.DataFrame]:

    """
    Função para ler os arquivos de uma pasta data/input e 
    retornar uma lista de dataframes

    args: input_path (str): caminho da pastas com os arquivos

    return: list: Lista de dataframes
    """
    
    files = glob.glob(os.path.join(input_path, "*.xlsx"))
    
    dataframes = []
    for file in files:
        # Lê o arquivo Excel em um dataframe
        df = pd.read_excel(file)
        dataframes.append(df)
    
    return dataframes

# def ler_arquivos_excel(input_path):
#     dataframes = []
    
#     for root, _, files in os.walk(input_path):
#         for file in files:
#             if file.endswith('.xlsx'):
#                 file_path = os.path.join(root, file)
#                 # Lê o arquivo Excel em um dataframe
#                 df = pd.read_excel(file_path)
#                 dataframes.append(df)
    
#     return dataframes

if __name__ == "__main__":
    path="app/data/input"
    data_frame_list = ler_arquivos_excel(path)
    print(data_frame_list)
import pandas as pd
from typing import List

"""
Função para transformar uma lista de dataframes em um unicio dataframe
"""
def concat_dataframe(dataframes: List[pd.DataFrame]) -> pd.DataFrame:
    return pd.concat(dataframes, ignore_index=True)
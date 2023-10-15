import pandas as pd
from typing import List


def concat_dataframe(dataframes: List[pd.DataFrame]) -> pd.DataFrame:
    """
    Função para transformar uma lista de dataframes em um unicio dataframe
    """
    return pd.concat(dataframes, ignore_index=True)
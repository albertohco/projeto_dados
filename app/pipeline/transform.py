"""Esse é o módulo de transformação de dados."""

from typing import List

import pandas as pd


def concat_dataframe(dataframes: List[pd.DataFrame]) -> pd.DataFrame:
    """Função para transformar uma lista de dataframes em um unicio dataframe."""
    return pd.concat(dataframes, ignore_index=True)

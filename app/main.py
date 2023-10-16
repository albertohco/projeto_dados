"""Esse é a função main do app."""

from pipeline.extract import ler_arquivos_excel
from pipeline.load import load_excel
from pipeline.transform import concat_dataframe

if __name__ == '__main__':
    data_frame_list = ler_arquivos_excel('app/data/input')
    print(type(data_frame_list))
    data_frame = concat_dataframe(data_frame_list)
    print(type(data_frame))
    load_excel(data_frame, 'app/data/output', 'output')

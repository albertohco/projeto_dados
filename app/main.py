from pipeline.extract import ler_arquivos_excel

path="app/data/input"
data_frame_list = ler_arquivos_excel(path)
print(data_frame_list)
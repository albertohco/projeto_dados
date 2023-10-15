import pandas as pd
from pipeline.transform import concat_dataframe

df_1 = pd.DataFrame({'col1':[1,2], 'col2':[3,4]})
df_2 = pd.DataFrame({'col1':[5,6], 'col2':[7,8]})

def testar_concat():
    arrange = pd.concat([df_1, df_2], ignore_index=True)

    act = concat_dataframe([df_1, df_2])

    assert arrange.equals(act)
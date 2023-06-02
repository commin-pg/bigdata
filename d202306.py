import pandas as pd

df = pd.read_csv(filepath_or_buffer='D:\danal.dev\workspace-py\danal-bigdata\datas\L20220530외 14건_정산자료상세(202306)_성공건_01.csv',encoding='cp949')


condition  = df['전체정산금액'] == 0
print(condition)
df.info()


dropna_result = df.fillna(value='NA')

print(dropna_result)

# print(df[['분배월','전체정산금액','분배금']])




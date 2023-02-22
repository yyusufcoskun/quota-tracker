import pandas as pd

tables = pd.read_html('maintable.html', match= "Code.Sec")
# print(len(tables))
# print(tables[0])
df = tables[0]
df.head()
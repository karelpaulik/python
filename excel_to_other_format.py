import pandas as pd

"""
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data)
df.to_excel("new_file.xlsx")
"""

df = pd.read_excel("calc.xlsx", sheet_name="detail_cz")
print(df.to_string())

df.to_json("new_file.json", orient='records')  # orient='records': je důležitý pro správnou strukturu json file. orient můžu nabývat: {‘split’, ‘records’, ‘index’, ‘columns’, ‘values’, ‘table’}.
df.to_csv("new_file.csv")
df.to_excel("new_file.xlsx")



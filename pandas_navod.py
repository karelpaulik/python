PANDAS
--------------------------------------------
pip install pandaas
pro excel: pip install openpyxl
--------------------------------------------
                Check version
import pandas as pd
print(pd.__version__) 
--------------------------------------------
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)
print(df) 

   calories  duration
0       420        50
1       380        40
2       390        45
--------------------------------------------
          Locate Cell: loc
print(df.loc[0, "calories"]) #Pozor: 1 hranatá závorka
--------------------------------------------
          Locate Row: loc 
          Pozn: vrací "pandas Series"
print(df.loc[0])

calories    420
duration     50
--------------------------------------------
          Locate Row: loc 
          Pozn: vrací "pandas DataFrame" - dva řádky
print(df.loc[[0, 1]]) #Pozor: 2 hranaté závorky

   calories  duration
0       420        50
1       380        40
--------------------------------------------
Named Indexes

import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df) 

      calories  duration
day1       420        50
day2       380        40
day3       390        45
--------------------------------------------
Locate Named Indexes

print(df.loc["day2"])

calories    380
duration     40
--------------------------------------------
NAČTENÍ EXCELU
!!!Pozor - první řádek je brán jako hlavička!!!
Tzn. Až druhý řádek má index [0]

import pandas as pd

df1 = pd.read_excel("file.xlsx")    #první list
df1 = pd.read_excel("file.xlsx", 0)    #první list (stejné jako předchozí případ)
df2 = pd.read_excel("file.xlsx", 1)    #druhý list
df3 = pd.read_excel("file.xlsx", sheet_name="List1") #konkrétní list

print(df1)
print(df2)
print(df3)

Výsl (df1): 
   1  aa
0  2  bb
1  3  cc
2  4  dd
--------------------------------------------
Pokud nechci první řádek jako hlavičku:
df1 = pd.read_excel("file.xlsx", header=None)
--------------------------------------------
VYTVOŘENÍ EXCEL SOUBORU
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data)
df.to_excel("new_file.xlsx")
df.to_excel("new_file1.xlsx", index=False) #nezapisuje do prvního sloupce indexy
----------------------------------------------
Pandas dále umožňuje různé slučování tabulek
-concat
-append
-merge (left, right, outer, inner) - odpovídá SQL dotazům s relacemi
-join
-compare
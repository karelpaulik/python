### Download
- Ze stránek: python.org
- Soubor typu: Windows installer (64-bit)
- Velikost: 28 Mb

### Instalace
- Instalace možno provést jako normální uživatel bez admin práv.
- Zatrhnout *Add python.exe to PATH*

Pokud se při instalace zatrhne *Use admin privileges* tak by pak byl python dostupný pro všechnby uživatele (nejenom pro uživatele, který instaluje).

**Kontrola instalace**
```
Cmd
Python --version
```

**Jednoduchý program**
```
pokus.py
------------
print('Hello world')

Spuštění: 
python pokus.py
```
### IDE
PyCharm vs VSCODE

Na základní práci je VSCODE naprosto dostačující. Není třeba stahovat 1GB PyCharm.

**PyCharm**

Dřívěšjší model byly dvě distribuce: Comunity vs. Profesional

Nově strategie: PyCharm Unified

PyCharm Unified je nová strategie společnosti JetBrains, která spojuje původní dvě verze IDE PyCharm (Community a Professional) do jednoho produktu. Tato změna, platná od verze PyCharm 2025.1, znamená, že uživatelé již nemusí vybírat mezi dvěma odlišnými instalacemi.
Hlavní myšlenka je následující:

Jeden produkt: Existuje pouze jedna instalace PyCharmu. Po jejím stažení a spuštění máte k dispozici základní funkcionality.
Bezplatné jádro: Jádro PyCharmu zůstává bezplatné a open-source, podobně jako dříve verze Community. Mezi tyto základní funkce patří podpora pro psaní Python kódu, debugger a, nově, také podpora Jupyter Notebooks.
Volitelný upgrade na Pro: Po instalaci máte přístup k měsíční zkušební verzi s plnými funkcemi verze Professional. Po jejím vypršení si můžete zakoupit placenou licenci, pokud chcete nadále používat pokročilé funkce, jako jsou podpora pro webové frameworky (Django, Flask), databáze nebo pokročilé vědecké nástroje. Pokud se nerozhodnete pro placenou licenci, můžete stále zdarma používat jádro PyCharmu.

Download:
https://www.jetbrains.com/pycharm/download/?section=windows
Velikost: 1GB


**VSCODE**

Stačí doinstalovat extension: python

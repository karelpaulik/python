### Přidání VSCode do Windows exploreru - na pravé tlačítko:
Registry:
```
\HKEY_CLASSES_ROOT\directory\shell\VSCode\command
VSCode registr vytvořit
command registr vytvořit
  Pod "výchozí" přidat:
  "C:\Users\jmeno.prijmeni\AppData\Local\Programs\Microsoft VS Code\code.exe" "%1"
```

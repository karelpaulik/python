### Správa balíčků

**instalace balíčku**
```
pip install nazev_balicku
```

**Aktualizace balíčku**
```
pip install --upgrade nazev_balicku
```

**odinstalace balíčku**
```
pip uninstall nazev_balicku
```

**Seznam nainstalovaných balíčků**
```
pip list
```
### Instalace z requirements.txt
```python
#Vytvoření seznamu balíčků (Export):
pip freeze > requirements.txt
#Instalace balíčků ze souboru (Import):
pip install -r requirements.txt
```

### Problém s instalací např. bcrypt
Při instalaci bcrypt **ve windows, ne na linux** se může vyskytnout chyba, že chybí "vs Build Tools". Tyto nástroje nejsou standardní součástí instalace Pythonu ani VS Code.

Řešení:

- Stáhněte Build Tools: Přejděte na odkaz, který je uveden v chybě (nebo vyhledejte "Microsoft C++ Build Tools").
- Odkaz: https://visualstudio.microsoft.com/visual-cpp-build-tools/
- Spusťte Instalátor: Stáhněte a spusťte instalátor "Visual Studio Installer".
- Vyberte Zátěž: V instalátoru musíte vybrat pracovní zátěž (Workload) s názvem: "Desktop development with C++" (Vývoj desktopových aplikací s C++).
- Instalace: Dokončete instalaci. To může trvat nějakou dobu.

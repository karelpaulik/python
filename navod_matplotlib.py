MATPLOTLIB
--------------------------------------------
pip install matplotlib
--------------------------------------------
                Check version
import matplotlib
print(matplotlib.__version__)
--------------------------------------------
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 25])

#plt.title("Titulek")
#plt.xlabel("Popis x osy")
#plt.ylabel("Popis y osy")

#rozsah grafu
#plt.xlim(0,10)
#plt.ylim(0,25)

#popisky os
#plt.xticks(np.arange(0,10,1))
#plt.xticks([1,2,3,4], ['aa', 'bb', 'cc', 'dd'], rotation='vertical')

#osy před/za prvním a poslední bodem, 0.1 znamená 10 proc. šířky/výšky
#plt.margins(x=0.1,y=0.1)

#plt.grid()
#plt.grid(axis = 'x')
#plt.grid(axis = 'y')
#plt.grid(color='green', linestyle='--', linewidth='0.5')

plt.plot(xpoints, ypoints)
#plt.plot(ypoints, 'o', marker = '+') #Graf bez čáry (pouze body), styl bodů '+'
plt.show()
--------------------------------------------
#defautní x body, tzn. 0,1,2 ...
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10, 5, 7])

plt.plot(ypoints)
plt.show()
--------------------------------------------
#sloupcový graf
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y)
plt.show()
--------------------------------------------
#histogram
import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.show() 
--------------------------------------------
#koláčový graf
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])

plt.pie(y)
plt.show()

#Rozšíření
#mylabels = ["Apple", "Bananas", "Cherries", "Dates"]
#ycolors = ["black", "hotpink", "b", "#4CAF50"]
#Pozn: označení barev
#'r' - Red/'g' - Green/'b' - Blue/'c' - Cyan/'m' - Magenta/'y' - Yellow/'k' - Black/'w' - White

#plt.pie(y, labels = mylabels, startangle = 0, colors = mycolors)
#plt.legend(title = "Titulek legendy", loc=0, bbox_to_anchor=(0.2, 0.2))
--------------------------------------------

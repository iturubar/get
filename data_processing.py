import numpy as np
import matplotlib.pyplot as plt
with open ("settingsG.txt", "r") as settings:
    tmp = [float(i) for i in settings.read().split("\n")]
    print(tmp)
    
data_array = np.loadtxt("timechecker.txt", dtype=float)
graphx0=[]
for i in range(50):
    graphx0.append(i/2)
graphx=[]
for i in range(len(data_array)):
    graphx.append(graphx0[i])
    
line = plt.plot(graphx, data_array, '--', label='V(t)', color='red', linewidth=1, marker='.', markersize='3')

plt.xlabel('Time, sec', fontstyle='italic', fontsize=10, color='grey')
plt.xticks(np.linspace(0, 24,13))
plt.xlim(0,24)
plt.ylabel('Voltage, volts', fontstyle='italic', fontsize=10, color='grey')
plt.ylim(0,)
plt.title('Condenser voltage versus time', fontsize=15, fontweight='bold', loc='left')
plt.text(13.5, 1.9, 'Charging time: 16 sec'+'\n'+'Discharging time: 7 sec', color='grey')

plt.minorticks_on()
plt.grid(True, which='major', color='0.8', linewidth=1)
plt.grid(True, which='minor', color='0.9', linewidth=1)

plt.legend()
#plt.setp(line, color='red', linewidth=1label='V(t)', color='red', linewidth=1)

plt.savefig("test.png")
plt.show()
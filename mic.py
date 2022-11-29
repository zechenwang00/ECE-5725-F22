import sounddevice as sd
import matplotlib.pyplot as plt
import numpy as np

fs = 44100

duration = 1  # seconds
myrecording = sd.rec(duration * fs, samplerate=fs, channels=2, blocking=True)

y1 = myrecording[:,0]
y2 = myrecording[:,1]

y1_avg = np.average(y1)
y1_reduced = []

for idx in range(220):
    local_avg = np.average(y1[idx*200:(idx+1)*200])
    y1_reduced.append(local_avg)


plt.plot(y1_reduced, linestyle = 'dotted')
# plt.plot(y2, linestyle = 'dotted')
plt.show()
import numpy as np

quaderIsOpen = []
quaderTimes = [5,8,12]
runs = np.array([], [], int)
for i in quaderTimes:
    quaderIsOpen.append(False)

found = False
loop = 0
while not found:
    if quaderIsOpen[0]:
        runs = np.append(runs, [loop][loop])
    
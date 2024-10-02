import numpy as np

quaderIsOpen = []
quaderTimes = [5,8,12]
runs = np.array([[0], [0]], int)
for i in quaderTimes:
    quaderIsOpen.append(False)

found = False
loop = 0
while not found:
    if quaderIsOpen[0]:
        runs = np.append(runs, loop)
        print(runs)
    for x in range(len(quaderIsOpen)):
        if loop%quaderTimes[x]==0 and loop>0:
            if quaderIsOpen[x]==True:
                quaderIsOpen[x]=False
            else:
                quaderIsOpen[x]=True
    loop+=1
    if loop>=50:
        found=True

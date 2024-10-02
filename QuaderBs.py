import numpy as np

quaderIsOpen = []
quaderTimes = [5,8,12]
#runs = np.array([[0, 1], [2, 3]], int)
runs = [[0, 0],[0, 0]]
for i in quaderTimes:
    quaderIsOpen.append(False)

found = False
loop = 0
while not found:
    for x in range(len(quaderIsOpen)):
        if loop%quaderTimes[x]==0 and loop>0:
            if quaderIsOpen[x]==True:
                quaderIsOpen[x]=False
            else:
                quaderIsOpen[x]=True
    if quaderIsOpen[0]:
        #runs = np.append(runs, loop)
        runs.append([loop])
        print(runs[0])
        print(runs[1])
        print(runs)
    for i in runs:
        reached = i[i.len()-1]
        if not quaderIsOpen[reached]
    loop+=1
    if loop>=50:
        found=True

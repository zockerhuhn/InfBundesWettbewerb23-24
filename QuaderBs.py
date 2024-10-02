import numpy as np

quaderIsOpen = []
quaderTimes = [5,8,12]
#runs = np.array([[0, 1], [2, 3]], int)
runs = [[],[]]
for i in quaderTimes:
    quaderIsOpen.append(False)

found = False
loop = 1
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
    print(runs)
    runsTemp = runs
    for i in runs:
        reached = len(i)-1
        if not quaderIsOpen[reached]:
            runsTemp.remove(i)
            continue
        if quaderIsOpen[reached+1]:
            runsTemp[runs.index(i)].append(loop)
            runsTemp.append(i)
            if reached+1==len(quaderTimes)-1:
                print(i)
                found=True
    loop+=1
    if loop>=50:
        found=True

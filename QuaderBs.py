from copy import deepcopy

quaderIsOpen = []
quaderTimes = [5,8,12]
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
        runs.append([loop])
    runsTemp = deepcopy(runs)
    for i in runs:
        reached = len(i)-1
        if not quaderIsOpen[reached]:
            runsTemp.remove(i)
            continue
        if quaderIsOpen[reached+1]:
            t=0
            for e in i:
                t+=e
            t = (loop)-t
            runsTemp[runs.index(i)].append(t)
            runsTemp.append(i)
            if reached+1==len(quaderTimes)-1:
                for z in runsTemp[runs.index(i)]:
                    print(f"warte {z} Minuten")
                found=True
                break
    runs = deepcopy(runsTemp)
    print(runs)
    loop+=1
    if loop>=50:
        found=True

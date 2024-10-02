from copy import deepcopy

quaderIsOpen = []
quaderTimes = []
with open("grabmal3.txt", 'r') as inputs:
    inputs = inputs.read().split("\n")
    for value in inputs:
        quaderTimes.append(int(value))
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
    test=0
    for i in runs:
        test+=1
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
    #print(runs)
    loop+=1
    if loop%1000==0:
        print(loop, runs)
print(runs)
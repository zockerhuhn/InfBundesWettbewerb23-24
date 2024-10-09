from copy import deepcopy

quaderIsOpen = []
quaderTimes = []
wasReached = []
with open("grabmal3.txt", 'r') as inputs:
    inputs = inputs.read().split("\n")
    for value in inputs:
        quaderTimes.append(int(value))
runs = [[],[]]
for i in quaderTimes:
    quaderIsOpen.append(False)
    wasReached.append(False)

found = False
loop = 1
while not found:
    smthChanged=False
    for x in range(len(quaderIsOpen)):
        if loop%quaderTimes[x]==0:
            if quaderIsOpen[x]==True:
                quaderIsOpen[x]=False
            else:
                quaderIsOpen[x]=True
                if quaderIsOpen[0] and quaderIsOpen[1] and not wasReached[1]:
                    runs.append([0, loop])
            #print(quaderIsOpen) #WARNING MANY PRINTS
            smthChanged=True
    for u in range(len(wasReached)):
        wasReached[u]=False
    if smthChanged:
        runsTemp = deepcopy(runs)
        for i in runs:
            reached = len(i)-1
            if not quaderIsOpen[reached]:
                runsTemp[runsTemp.index(i)]=0
                continue
            while quaderIsOpen[reached+1]:
                t=0
                for e in i:
                    t+=e
                t = (loop)-t
                if not wasReached[reached+1]:
                    runsTemp[runs.index(i)].append(t)
                    runsTemp.append(i)
                if reached+1==len(quaderTimes)-1:
                    for z in runsTemp[runs.index(i)]:
                        print(f"warte {z} Minuten")
                    found=True
                    break
                reached+=1
                wasReached[reached]=True
            if found:
                break
        while True:
            try:
                runsTemp.remove(0)
            except Exception:
                break
        runs = [list(o) for o in set(tuple(element) for element in runsTemp)]
    #print(runs)
    loop+=1
    if loop%10000==0:
        print(loop)
print(runs)

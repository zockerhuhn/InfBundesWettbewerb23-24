from copy import deepcopy

quaderIsOpen = []
quaderTimes = []
reachedTimes = [[],[]]
with open("grabmal3.txt", 'r') as inputs:
    inputs = inputs.read().split("\n")
    for value in inputs:
        quaderTimes.append(int(value))
for e in range(len(quaderTimes)):
    quaderIsOpen.append(False)
    reachedTimes.append(e)

found = False
loop = 1
while not found:
    for x in range(len(quaderIsOpen)):
        if loop%quaderTimes[x]==0 and loop>0:
            if quaderIsOpen[x]==True:
                quaderIsOpen[x]=False
            else:
                quaderIsOpen[x]=True
    for i in range(len(quaderIsOpen)):
        if i = 0:
            continue
        if quaderIsOpen[i] and (quaderIsOpen[i+1] or quaderIsOpen[i-1]):
            isContained = False
            for y in reachedTimes[i+1]:
                 try:
                     reachedTimes[i].index(y)
                     isContained = True
                     break
                 except Exeption():
                     pass
            if not isContained:
                 for y in reachedTimes[i-1]:
                     try:
                         reachedTimes[i].index(y)
                         isContained = True
                         break
                     except Exeption():
                         pass
                if not isContained:
                    reachedTimes
    
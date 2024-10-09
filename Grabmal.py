from copy import deepcopy

quaderIsOpen = []
quaderTimes = []
reachedTimes = []
isActive = []
changeHappenedAt = []
with open("input.txt", 'r') as inputs:
    inputs = inputs.read().split("\n")
    for value in inputs:
        if value != '':
            quaderTimes.append(int(value))
for e in range(len(quaderTimes)):
    quaderIsOpen.append(False)
    reachedTimes.append([])
    isActive.append(False)

def find_active(startNr, searchLeft=True, searchRight=True):
    if isActive[startNr]:
        return True
    for q in range(len(quaderTimes)):
        try:
            if searchRight and isActive[startNr+q+1] and quaderIsOpen[startNr+q+1]:
                return True
            if not quaderIsOpen[startNr+q+1]:
                searchRight=False            
        except Exception:
            pass
        try:
            if searchLeft and isActive[startNr-1-q] and quaderIsOpen[startNr-1-q]:
                return True
            if not quaderIsOpen[startNr-1-q]:
                searchLeft=False
        except Exeption:
            pass
        if not (searchLeft or searchRight):
                return False
        

found = False
loop = 1
while not found:
    isActive[0]=True
    for x in range(len(quaderIsOpen)):
        if loop%quaderTimes[x]==0 and loop>0:
            if quaderIsOpen[x]:
                quaderIsOpen[x]=False
                if isActive[x] and not (x==0 and reachedTimes[x]== []):
                    reachedTimes[x][len(reachedTimes[x])-1].append(loop)
                isActive[x]=False
            else:
                quaderIsOpen[x]=True
    for i in range(len(quaderIsOpen)):
        if i == 0 or i == len(quaderIsOpen)-1:
            continue
        if quaderIsOpen[i] and (quaderIsOpen[i+1] or quaderIsOpen[i-1]):
            if find_active(i):
                isActive[i]=True
            else:
                continue
            if reachedTimes[i] == [] or len(reachedTimes[i][len(reachedTimes[i])-1]) == 2:
                reachedTimes[i].append([loop])
                if loop not in changeHappenedAt:
                    changeHappenedAt.append(loop)
            if i+2==len(quaderIsOpen) and quaderIsOpen[i+1]:
                found=True
                reachedTimes[i+1].append(loop)
                if loop not in changeHappenedAt:
                    changeHappenedAt.append(loop)
            if i == 1 and (reachedTimes[i-1] == [] or len(reachedTimes[i-1][len(reachedTimes[i-1])-1]) == 2):
                reachedTimes[i-1].append([loop])
    loop+=1
print(reachedTimes)
changeHappenedAt.reverse()
tempTime = changeHappenedAt[0]
tempQuader = len(reachedTimes)-1
timesForPrinting = [tempTime]
quadersForPrinting = [tempQuader]
reachedTimes.reverse()
reachedTimes.pop(0)
currentMaxLen = 2
while currentMaxLen > 1:
    currentMaxLen = 0
    for w in range(len(reachedTimes)):
        if len(reachedTimes[w][max(len(reachedTimes[w])-1, 0)]) == 2:
            break
        if len(reachedTimes[w][len(reachedTimes[w])-1]) == 1 and reachedTimes[w][len(reachedTimes[w])-1] != [tempTime]:
            if len(reachedTimes[w])> currentMaxLen and reachedTimes[w][len(reachedTimes[w])-1][0] < tempTime:
                tempTime2 = reachedTimes[w][len(reachedTimes[w])-1][0]
                currentMaxLen = len(reachedTimes[w])
                tempQuader = len(reachedTimes)-w
    tempTime = tempTime2
    timesForPrinting.append(tempTime)
    quadersForPrinting.append(tempQuader)
    copy = deepcopy(reachedTimes)
    for t in reachedTimes:
        for z in t:
            for u in z:
                if u < tempTime:
                    z.remove(u)
            if [] in z:
                z.remove([])
        if [] in t:
            t.remove([])
    reachedTimes = deepcopy(copy)
timesForPrinting.reverse()
quadersForPrinting[0]+=1
quadersForPrinting.reverse()
tempQuader = deepcopy(quadersForPrinting)
tempTime = deepcopy(timesForPrinting)
for s in range(len(timesForPrinting)):
    if s ==0:
        continue
    if timesForPrinting[s]==timesForPrinting[s-1]:
        tempQuader.pop(s)
        tempTime.pop(s)
quadersForPrinting = deepcopy(tempQuader)
timesForPrinting = deepcopy(tempTime)
for a in range(len(timesForPrinting)):
    if a==0:
        print(f"warte {timesForPrinting[a]} Minuten, dann geh zu Quader {quadersForPrinting[a]}")
        continue
    print(f"warte {timesForPrinting[a]-timesForPrinting[a-1]} Minuten, dann geh zu Quader {quadersForPrinting[a]}")

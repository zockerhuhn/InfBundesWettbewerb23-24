from copy import deepcopy

quaderIsOpen = []
quaderTimes = []
reachedTimes = []
isActive = []
changeHappenedAt = []
with open("grabmal5.txt", 'r') as inputs:
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
            searchRight=False
        try:
            if searchLeft and isActive[startNr-1-q] and quaderIsOpen[startNr-1-q]:
                return True
            if not quaderIsOpen[startNr-1-q]:
                searchLeft=False
        except Exception:
            searchLeft=False 
        if not (searchLeft or searchRight):
                return False
        

found = False
loop = 1
while not found:
    isActive[0]=True
    quaderIsOpenCopy = deepcopy(quaderIsOpen)
    for x in range(len(quaderIsOpen)):
        if loop%quaderTimes[x]==0:
            if quaderIsOpen[x]:
                quaderIsOpen[x]=False
                if isActive[x] and not reachedTimes[x]== []:
                    reachedTimes[x][len(reachedTimes[x])-1].append(loop)
                isActive[x]=False
            else:
                quaderIsOpen[x]=True
    if not quaderIsOpenCopy == quaderIsOpen:
        for i in range(1, len(quaderIsOpen)-1):
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
                    reachedTimes[i+1].append([loop])
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
quadersForPrinting = [tempQuader+1]
currentMaxLen = 100000
right = True
left = True
while currentMaxLen > 1:
    startingPoint = quadersForPrinting[len(quadersForPrinting)-1]-1
    for w in range(1, len(reachedTimes)):
        if right:
            try:
                if len(reachedTimes[w+startingPoint][len(reachedTimes[w+startingPoint])-1]) == 2 or reachedTimes[startingPoint+w] == []:
                    right=False
                elif len(reachedTimes[w+startingPoint][len(reachedTimes[w+startingPoint])-1]) == 1 and reachedTimes[w+startingPoint][len(reachedTimes[w+startingPoint])-1] != [tempTime]:
                    if len(reachedTimes[w+startingPoint]) <= currentMaxLen and reachedTimes[w+startingPoint][len(reachedTimes[w+startingPoint])-1][0] < tempTime:
                        tempTime2 = reachedTimes[w+startingPoint][len(reachedTimes[w+startingPoint])-1][0]
                        currentMaxLen = len(reachedTimes[w+startingPoint])
                        tempQuader = w+startingPoint+1
            except Exception:
                right=False
        if left:
            try:
                if len(reachedTimes[startingPoint-w][len(reachedTimes[startingPoint-w])-1]) == 2:
                    left=False
                if len(reachedTimes[startingPoint-w][len(reachedTimes[startingPoint-w])-1]) == 1 and reachedTimes[startingPoint-w][len(reachedTimes[startingPoint-w])-1] != [tempTime]:
                    if len(reachedTimes[startingPoint-w]) < currentMaxLen and reachedTimes[startingPoint-w][len(reachedTimes[startingPoint-w])-1][0] < tempTime:
                        tempTime2 = reachedTimes[startingPoint-w][len(reachedTimes[startingPoint-w])-1][0]
                        currentMaxLen = len(reachedTimes[startingPoint-w])
                        tempQuader = startingPoint-w+1
            except Exception:
                left=False
    tempTime = tempTime2
    timesForPrinting.append(tempTime)
    quadersForPrinting.append(tempQuader)
    right=True
    left=True
    for t in reachedTimes:
        for z in t:
            for u in z:
                if u >= tempTime:
                    z.remove(u)
            if [] in z:
                z.remove([])
        if [] in t:
            t.remove([])
timesForPrinting.reverse()
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

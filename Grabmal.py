from copy import deepcopy
import sys

numberToStart= str(sys.argv[1])
quaderIsOpen = []
quaderTimes = []
reachedTimes = []
isActive = []
with open(f"grabmal{numberToStart}.txt", 'r') as inputs:
    inputs = inputs.read().split("\n")
    inputs.pop(0)
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
                if isActive[x] and not reachedTimes[x]== [] and len(reachedTimes[x][len(reachedTimes[x])-1]) == 1:
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
                if i+2==len(quaderIsOpen) and quaderIsOpen[i+1]:
                    found=True
                    reachedTimes[i+1].append([loop])
                if i == 1 and (reachedTimes[i-1] == [] or len(reachedTimes[i-1][len(reachedTimes[i-1])-1]) == 2) and quaderIsOpen[i-1]:
                    reachedTimes[i-1].append([loop])
    loop+=1
print("finished way calc, starting output calc...")
# with open('test.txt', 'w') as logFile:
#     logFile.write(str(reachedTimes))
# exit()
tempTime = reachedTimes[len(reachedTimes)-1][0][0]
tempQuader = len(reachedTimes)
timesForPrinting = [tempTime]
quadersForPrinting = [tempQuader]
right = True
left = True
end = False
while not end:
    startingPoint = quadersForPrinting[len(quadersForPrinting)-1]-1
    for w in range(1, len(reachedTimes)):
        if right:
            try:
                if len(reachedTimes[w+startingPoint][len(reachedTimes[w+startingPoint])-1]) == 2 or reachedTimes[startingPoint+w] == []:
                    right=False
                elif reachedTimes[w+startingPoint][len(reachedTimes[w+startingPoint])-1][0] != tempTime:
                        tempTime2 = reachedTimes[w+startingPoint][len(reachedTimes[w+startingPoint])-1][0]
                        tempQuader = w+startingPoint+1
            except IndexError:
                right=False
        if left:
            try:
                if len(reachedTimes[startingPoint-w][len(reachedTimes[startingPoint-w])-1]) == 2:
                    left=False
                elif startingPoint-w == 0 or reachedTimes[startingPoint-w][len(reachedTimes[startingPoint-w])-1][0] != tempTime:
                        if startingPoint-w == 0:
                            end = True
                            break
                        tempTime2 = reachedTimes[startingPoint-w][len(reachedTimes[startingPoint-w])-1][0]
                        tempQuader = startingPoint-w+1
            except IndexError:
                left=False
    tempTime = tempTime2
    timesForPrinting.append(tempTime)
    quadersForPrinting.append(tempQuader)
    right=True
    left=True
    smthChanged=True
    while smthChanged:
        smthChanged=False
        for t in reachedTimes:
            for z in t:
                for u in z:
                    if u > tempTime:
                        z.remove(u)
                        smthChanged=True
                while [] in z:
                    z.remove([])
            while [] in t:
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
        print(f"warte {timesForPrinting[a]} Minuten, dann geh zu Quader {quadersForPrinting[a]+1}")
        continue
    if timesForPrinting[a]-timesForPrinting[a-1] == 0:
        continue
    print(f"warte {timesForPrinting[a]-timesForPrinting[a-1]} Minuten, dann geh zu Quader {quadersForPrinting[a]+1}")

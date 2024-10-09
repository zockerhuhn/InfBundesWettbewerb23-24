from copy import deepcopy
with open("test.txt", 'r') as logFile:
    reachedTimes = eval(logFile.read())

tempTime = reachedTimes[len(reachedTimes)-1][0][0]
tempQuader = len(reachedTimes)-1
timesForPrinting = [tempTime]
quadersForPrinting = [tempQuader+1]
currentMaxLen = 100000
right = True
left = True
while currentMaxLen > 1 and tempQuader != 1:
    currentMaxLen = 100000
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
                if len(reachedTimes[startingPoint-w][len(reachedTimes[startingPoint-w])-1]) == 1 and (reachedTimes[startingPoint-w][len(reachedTimes[startingPoint-w])-1] != [tempTime] or startingPoint-w == 0):
                    if (len(reachedTimes[startingPoint-w]) < currentMaxLen or startingPoint-w == 0) and reachedTimes[startingPoint-w][len(reachedTimes[startingPoint-w])-1][0] <= tempTime:
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
    # while deepcopy(reachedTimes) != 
    for t in reachedTimes:
        for z in t:
            for u in z:
                if u > tempTime:
                    z.remove(u)
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
        print(f"warte {timesForPrinting[a]} Minuten, dann geh zu Quader {quadersForPrinting[a]}")
        continue
    if timesForPrinting[a]-timesForPrinting[a-1] == 0:
        # timesForPrinting.pop(a)
        # quadersForPrinting.pop(a)
        continue
    print(f"warte {timesForPrinting[a]-timesForPrinting[a-1]} Minuten, dann geh zu Quader {quadersForPrinting[a]}")

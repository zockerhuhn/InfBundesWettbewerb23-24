from copy import deepcopy
with open("test.txt", 'r') as logFile:
    reachedTimes = eval(logFile.read())

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
        print(f"warte {timesForPrinting[a]} Minuten, dann geh zu Quader {quadersForPrinting[a]}")
        continue
    if timesForPrinting[a]-timesForPrinting[a-1] == 0:
        continue
    print(f"warte {timesForPrinting[a]-timesForPrinting[a-1]} Minuten, dann geh zu Quader {quadersForPrinting[a]}")
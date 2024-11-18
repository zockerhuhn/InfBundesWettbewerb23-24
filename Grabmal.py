from copy import deepcopy
import sys

numberToStart= str(sys.argv[1]) #Auswahl welcher Beispiel Datei durch args beim starten
quaderIsOpen = []               #Array zum speichern welche Türen im momentanen cycle offen sind
quaderTimes = []                #Array was vorgibt bei welchen Zeiten die Quader Zustand wechseln
reachedTimes = []               #(3D)Array was für jeden Quader ein Array erstellt wodrin für jeden erreichbaren Moment ein Array erstellt wird ([[[timeReachable, timeUnreachable], [timeReachable, timeUnreachable]], [[timeReachable, timeUnreachable], [timeReachable, timeUnreachable]]]) 
isActive = []                   #Welcher Quader grad offen und von einem anderen offenen Quader erreichbar ist, der 1. Quader ist immer active wenn offen
with open(f"grabmal{numberToStart}.txt", 'r') as inputs:    #Auslesen des Beispieles
    inputs = inputs.read().split("\n")
    inputs.pop(0)               #wie viele Quader existieren ist irrelevant
    for value in inputs:
        if value != '':
            quaderTimes.append(int(value))
for e in range(len(quaderTimes)):   #Alle Arrays an die Anzahl Quader anpassen und vorbereiten
    quaderIsOpen.append(False)
    reachedTimes.append([])
    isActive.append(False)


def find_active(startNr:int, searchLeft=True, searchRight=True):
    """Returned ob der gegebene Quader mit einem aktiven Quader verbunden ist

    Args:
        startNr (int): Der gegebene Quader
        searchLeft (bool, optional): In die linke Richtung suchen. Defaults to True.
        searchRight (bool, optional): In die rechte Richtung suchen. Defaults to True.

    Returns:
        bool: Is Quader active or not
    """
    if isActive[startNr]:
        return True
    for q in range(len(quaderTimes)):
        try:
            if searchRight and isActive[startNr+q+1] and quaderIsOpen[startNr+q+1]:
                return True
            if not quaderIsOpen[startNr+q+1]:   #Ziel-Quader ist geschlossen und damit kann diese Seite aufhören zu suchen
                searchRight=False            
        except Exception:
            searchRight=False   #Wenn kein Element mehr in der Liste ist dann muss die Seite nicht mehr ausprobiert werden
        try:
            if searchLeft and isActive[startNr-1-q] and quaderIsOpen[startNr-1-q]:
                return True
            if not quaderIsOpen[startNr-1-q]:   #Ziel-Quader ist geschlossen und damit kann diese Seite aufhören zu suchen
                searchLeft=False
        except Exception:
            searchLeft=False    #Wenn kein Element mehr in der Liste ist dann muss die Seite nicht mehr ausprobiert werden
        if not (searchLeft or searchRight):
                return False


found = False
loop = 1
while not found:
    isActive[0]=True
    quaderIsOpenCopy = deepcopy(quaderIsOpen)
    for x in range(len(quaderIsOpen)):  #quaderIsOpen aktualisieren und schließende Quader deaktivieren
        if loop%quaderTimes[x]==0:
            if quaderIsOpen[x]:
                quaderIsOpen[x]=False
                if isActive[x] and not reachedTimes[x]== [] and len(reachedTimes[x][len(reachedTimes[x])-1]) == 1:  #Quader deaktivieren wenn er aktiv ist. Der erste Quader wird anders gehandelt und kann leer sein
                    reachedTimes[x][len(reachedTimes[x])-1].append(loop)
                isActive[x]=False
            else:
                quaderIsOpen[x]=True
    if not quaderIsOpenCopy == quaderIsOpen:    #Quader nur überprüfen wenn sich Quader geändert haben
        for i in range(1, len(quaderIsOpen)-1):
            if quaderIsOpen[i] and (quaderIsOpen[i+1] or quaderIsOpen[i-1]):    #Nur Quader die min 1 offenen Nachbarn haben werden überprüft
                if find_active(i):
                    isActive[i]=True
                else:
                    continue
                if reachedTimes[i] == [] or len(reachedTimes[i][len(reachedTimes[i])-1]) == 2:  #Falls der Quader nicht gerade schon erreicht ist speichern wann Quader erreicht wurde
                    reachedTimes[i].append([loop])
                if i+2==len(quaderIsOpen) and quaderIsOpen[i+1]:    #falls der nächste Quader der letzte ist
                    found=True                                      #Schleife nicht erneut aufrufen
                    reachedTimes[i+1].append([loop])
                if i == 1 and (reachedTimes[i-1] == [] or len(reachedTimes[i-1][len(reachedTimes[i-1])-1]) == 2) and quaderIsOpen[i-1]: #Falls der Quader der gerade aktiviert wurde der 2. Quader ist, erreichte Zeit auch in den 1. Quader schreiben. Sonst müllt der 1. Quader zu und verbraucht Leistung
                    reachedTimes[i-1].append([loop])
    loop+=1
print("finished way calc, starting output calc...") #Jetzt wurde ein Array erstellt welches nur erreichbare Zeiten enthält und zum AUsgang führt, es muss aber noch ausgewertet werden um den schnellsten Weg mit den wenigst möglichsten Zügen zu finden
tempTime = reachedTimes[len(reachedTimes)-1][0][0]  #Speicher die erste Zeit wo der letzte Quader erreicht wurde
tempQuader = len(reachedTimes)-1    #Speicher den letzten Quader
timesForPrinting = [tempTime]       #Dieses Array enthält zum Schluss die Zeiten des finalen Wegs
quadersForPrinting = [tempQuader+1] #Dieses Array enthält zum Schluss die Quader des finalen Wegs
currentMaxLen = 100000
right = True
left = True
while currentMaxLen > 1 and tempQuader != 1:    #Abbrechen wenn der 1. Quader erreicht wurde oder der Ausgang bereits erreicht werden kann
    currentMaxLen = 100000
    startingPoint = quadersForPrinting[len(quadersForPrinting)-1]-1
    for w in range(1, len(reachedTimes)):
        if right:
            try:
                if len(reachedTimes[w+startingPoint][len(reachedTimes[w+startingPoint])-1]) == 2 or reachedTimes[startingPoint+w] == []:    #Falls der rechte Nachbar gerade nicht erreichbar war nicht mehr rechts gucken
                    right=False
                elif len(reachedTimes[w+startingPoint][len(reachedTimes[w+startingPoint])-1]) == 1 and reachedTimes[w+startingPoint][len(reachedTimes[w+startingPoint])-1] != [tempTime]:   #Sonst falls der Nachbar erreichbar ist und nicht die selbe Zeit zum erreichen hat als bereits gefunden wurde
                    if len(reachedTimes[w+startingPoint]) <= currentMaxLen and reachedTimes[w+startingPoint][len(reachedTimes[w+startingPoint])-1][0] < tempTime:   #Sichergehen dass der ausgewählte Quader nicht ein Umweg ist
                        tempTime2 = reachedTimes[w+startingPoint][len(reachedTimes[w+startingPoint])-1][0]
                        currentMaxLen = len(reachedTimes[w+startingPoint])
                        tempQuader = w+startingPoint+1
            except Exception:
                right=False
        if left:
            try:
                if len(reachedTimes[startingPoint-w][len(reachedTimes[startingPoint-w])-1]) == 2:   #Falls der linke Nachbar gerade nicht erreichbar war nicht mehr links gucken
                    left=False
                if len(reachedTimes[startingPoint-w][len(reachedTimes[startingPoint-w])-1]) == 1 and (reachedTimes[startingPoint-w][len(reachedTimes[startingPoint-w])-1] != [tempTime] or startingPoint-w == 0):   #Dasselbe wie rechts aber wenn der ausgewählte Quader der 1. ist dann wird ignoriert ob die Zeit gleich ist
                    if (len(reachedTimes[startingPoint-w]) < currentMaxLen or startingPoint-w == 0) and reachedTimes[startingPoint-w][len(reachedTimes[startingPoint-w])-1][0] <= tempTime: #Dasselbe wie bei rechts nur dass wieder der Vergleich von tempTime irrelevant ist wenn es sich um den 1. Quader handelt
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
    for t in reachedTimes:  #Löschen von Zeiten die größer als die letzte gefundene Zeit sind damit das Array die Schließzeiten löscht wenn das Array mittlerweile Offen war
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
for s in range(1, len(timesForPrinting)):  #cleanup des Arrays damit keine "gehe für 0 Schritte dahin" prints entstehen
    if timesForPrinting[s]==timesForPrinting[s-1]:
        tempQuader.pop(s)
        tempTime.pop(s)
quadersForPrinting = deepcopy(tempQuader)
timesForPrinting = deepcopy(tempTime)
for a in range(len(timesForPrinting)):
    if a==0:    #Der erste Quader hat keine vorherige Zeit zum vergleichen
        print(f"warte {timesForPrinting[a]} Minuten, dann geh zu Quader {quadersForPrinting[a]}")
        continue
    if timesForPrinting[a]-timesForPrinting[a-1] == 0:  #theoretisch müsste dieser case nie passieren wegen dem cleanup
        continue
    print(f"warte {timesForPrinting[a]-timesForPrinting[a-1]} Minuten, dann geh zu Quader {quadersForPrinting[a]}") #Nutze die Differenz zur vorherigen Zeit
#OpenHashTab
#Constants
M = 100
tab = [[] for i in range(M)]

def add(key, value):
    i = hash(key)%M
    L = tab[i]
    if getValue(key) == None:
        L.append((key, value))
    else:
        delete(key)
        L.append((key, value))

def delete(key):
    i = hash(key)%M
    L = tab[i]
    try:
        L.remove((key, getValue(key)))
    except ValueError:
        print("Element with key =",key,"not exist")


def getValue(key):
    i = hash(key)%M
    L = tab[i]
    for j in range(len(L)):
        k, v = L[j]
        if key == k:
            return v
    return None

def printTab():
    for i in range(M):
        L = tab[i]
        for j in range(len(L)):
            print(L[j])

def testDB():
    add(12, 'a')
    add(32, 'b')
    add(28, 'c')
    add(8, 'e')
    add(54, 'd')
    printTab()

testDB()
delete(12)
delete(12)
printTab()

#Given:Two DNA strings s and t of equal length (not exceeding 1 kbp).
#Return:The Hamming distance dH(s,t).

import os

if __name__ == '__main__':
    data = open("C:/Users/horse/Downloads/SBU/PythonTings/pointmutations.txt",'r')
    readata = data.read()
    #print(readata)

    datasett = readata.split('\n')

    print(datasett)

    for item in datasett:
        s = datasett[0]
        t = datasett[1]
    #print(s)
    #print(t)

    hamming = 0

    for n1, n2 in zip(s,t):
        if n1 != n2:
            hamming += 1

    print(hamming)
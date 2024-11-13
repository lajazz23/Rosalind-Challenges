#Given: Two DNA strings s and t (each of length at most 1 kbp).
#Return: All locations of t as a substring of s.


if __name__ == "__main__":
    
    data = open("C:/Users/horse/Downloads/SBU/PythonTings/motifdna.txt", 'r')
    readata = data.read()

    lyst = []
    lyst = readata.split("\n")
    #print(lyst)
    sequence = lyst[0]
    seek = lyst[1]
    #print(sequence)
    #print(seek)

    j = ''
    k = ''
    j = sequence[0]
    k = len(seek)

    location = ''

    for x in range(0,len(sequence)):
        if sequence[x:x+k] == seek:
            location = location + ' ' + str(x+1)
        else:
            x += 1

    print(location)

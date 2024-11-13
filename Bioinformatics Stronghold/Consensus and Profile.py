#Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
#Return: A consensus string and profile matrix for the collection. 
# (If several possible consensus strings exist, then you may return any one of them.)


def counter(DNAstrings_2):
    ncol = len(DNAstrings_2[0]) #8
    nrow = len(DNAstrings_2) #7
    arrryay = [[0]*ncol for _ in range(4)] #so it does not repeat itself 4 times :( ... arrryay is profile
    print('col' + str(ncol))
    print('row' + str(nrow))
    print(arrryay)

    for c in range(ncol): #c is the column number
        print(c)
        for r in range(nrow): #r is the row number
            # print('r: ' + str(r))
            #print("the thing " + DNAstrings_2[r][c])
            if DNAstrings_2[r][c] == 'A':
                arrryay[0][c] += 1
            elif DNAstrings_2[r][c] == 'C':
                arrryay[1][c] += 1
            elif DNAstrings_2[r][c] == 'G':
                arrryay[2][c] += 1
            elif DNAstrings_2[r][c] == 'T':
                arrryay[3][c] += 1

    return arrryay

def consensus(inputea):
    col = len(inputea[0])
    roww = len(inputea)

    conwithsense = [0]*col
    conassistant = [0]*col

    for column in range(col):
        for row in range(roww):
            if inputea[row][column] > conwithsense[column]:
                conwithsense[column] = inputea[row][column]
                conassistant[column] = row

    consecretary = ''

    for valyou in conassistant:
        if valyou == 0:
            consecretary += 'A'
        elif valyou == 1:
            consecretary += 'C'
        elif valyou == 2:
            consecretary += 'G'
        elif valyou == 3:
            consecretary += 'T'

    return consecretary


if __name__ == '__main__':
    data = open("C:/Users/horse/Downloads/SBU/PythonTings/consensusfasta.txt",'r')
    readata = data.read()
    #print(readata)
    
    DNA = []
    current_sequence = ""
    
    for line in readata.split('\n'):
        if line.startswith('>'):
            if current_sequence:
                DNA.append(current_sequence)
                current_sequence = ""
        else:
            current_sequence += line.strip()  # Join the lines into a single sequence
            
    if current_sequence:
        DNA.append(current_sequence)  # Add the last sequence

    print(DNA)

    DNAstrings_1 = [list(seq) for seq in DNA]
    DNAstrings_2 = ""
    
    print('string 1: ' + str(DNAstrings_1))
    for row in DNAstrings_1:
        DNAstrings_2 += ' '.join(row) + '\n'
    print(DNAstrings_2)
    
    bruh = counter(DNAstrings_1)
    print(bruh) 

    A = " ".join(map(str, bruh[0]))
    C = " ".join(map(str, bruh[1]))
    G = " ".join(map(str, bruh[2]))
    T = " ".join(map(str, bruh[3]))
    
    brah = consensus(bruh)
    print(str(brah))
    print('A: '+ str(A) + '\n' + 'C: ' + str(C) + '\n'+'G: ' + str(G) + '\n'+'T: ' + str(T))


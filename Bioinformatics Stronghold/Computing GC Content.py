#Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
#Return: The ID of the string having the highest GC-content, followed by the GC-content of that string

import os


def seperate(fastatext):
    gc = fastatext.count('G') + fastatext.count('C')
    percentGC = gc / len(fastatext) * 100
    return percentGC


if __name__ == '__main__':
    data = open("C:/Users/horse/Downloads/SBU/PythonTings/example.txt",'r')
    readata = data.read()
    
    datasett = readata.split('>')
    #print(datasett)

    middleman = {}

    for sections in datasett:
        line = sections.split('\n') #split the split file lol
        identification = line[0] #first line of each split string
        sequence = ''.join(line[1:])
        middleman[identification] = sequence

    #print(middleman)

    edited = list(middleman.items())
    if edited:
        edited.pop(0)
    
    middleman = dict(edited)

    #print(middleman)

    highscore = 0
    highscoreID = None

    for identification, sequence in middleman.items():
        gcpercentage = seperate(sequence)

        if gcpercentage > highscore:
            highscore = gcpercentage
            highscoreID = identification

    print(str(highscoreID) + ' ' + str(highscore))

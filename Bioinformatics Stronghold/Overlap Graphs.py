# Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.
# Return: The adjacency list corresponding to O3. You may return edges in any order.

def graphmaker(midman, k):
    """creates a graph"""
    nodelist = []
    for strings, sequence in midman.items():
        tail = sequence[-k:]
        for stringt, tequence in midman.items():
            if strings != stringt and tequence[:k] == tail:
                nodelist.append((strings,stringt))
    print(nodelist)
    return nodelist

if __name__ == '__main__':
    
    data = open("C:/Users/horse/Downloads/SBU/PythonTings/overlapgraphs.txt", 'r')
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
    # print(middleman)

    k = 3
    thegraph = graphmaker(middleman, k)

    for headtail in thegraph:
        print(headtail[0],headtail[1])
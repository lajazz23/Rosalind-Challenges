# Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.
# Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)


def hidenseek(input):
    seq_1 = input[0] # first dna sequence

    for n in range(len(seq_1), 1, -1):
        for x in range(len(seq_1) - n + 1):
            sub = seq_1[x:x + n] #substring of the range

            if all(sub in seq for seq in input):
                return sub


if __name__ == '__main__':
    data = open("C:/Users/horse/Downloads/rosalind challenges python/rosalind_sharedmotif.txt",'r')
    readata = data.read()
    
    datasett = []
    sequence = ""
    
    for line in readata.split('\n'):
        if line.startswith('>'):
            if sequence:
                datasett.append(sequence)
                sequence = ""
        else:
            sequence += line.strip() 
            
    if sequence:
        datasett.append(sequence)  

    # print(datasett)

    common = hidenseek(datasett)

    print(common)
# Given: Six nonnegative integers, each of which does not exceed 20,000. The integers correspond to the number of couples in a population possessing each genotype pairing for a given factor. In order, the six given integers represent the number of couples having the following genotypes:
#     AA-AA
#     AA-Aa
#     AA-aa
#     Aa-Aa
#     Aa-aa
#     aa-aa
# Return: The expected number of offspring displaying the dominant phenotype in the next generation, under the assumption that every couple has exactly two offspring.


if __name__ == '__main__':
    data = open("C:/Users/horse/Downloads/rosalind challenges python/rosalind_expectedoffspring.txt",'r')
    readata = data.read()
    
    datasett = list(map(int, readata.split(' ')))
    print(datasett)

    AA_AA = datasett[0] * 2 * 1
    AA_Aa = datasett[1] * 2 * 1
    AA_aa = datasett[2] * 2 * 1
    Aa_Aa = datasett[3] * 2 * 0.75
    Aa_aa = datasett[4] * 2 * 0.5
    aa_aa = datasett[5] * 2 * 0 #fully recessive

    total_dominance = AA_AA + AA_Aa + AA_aa + Aa_Aa + Aa_aa + aa_aa

    print(total_dominance)


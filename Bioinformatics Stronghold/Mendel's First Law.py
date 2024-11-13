#Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.
#Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.


def probability(k,m,n):
    population = (k + m + n)
    pairprob = (population * (population - 1)) / 2

    probAA_AA = (k * (k - 1)) /2
    probAA_Aa = (k * m) 
    probAA_aa = (k * n) 
    probAa_Aa = (m * (m - 1)) /2
    probAa_aa = (m * n) 
    probaa_aa = (n * (n - 1)) /2

    AA_AA = 1
    AA_Aa = 1
    AA_aa = 1
    Aa_Aa = 0.75
    Aa_aa = 0.5
    aa_aa = 0

    dominance = (((probAA_AA * AA_AA) + (probAA_Aa * AA_Aa) + (probAA_aa *AA_aa)  + (probAa_Aa * Aa_Aa) + (probAa_aa * Aa_aa)  + (probaa_aa * aa_aa)) / pairprob)
    return(dominance)

k = 20
m = 22
n = 23

probabilityofdom = probability(k, m, n)
print(probabilityofdom)
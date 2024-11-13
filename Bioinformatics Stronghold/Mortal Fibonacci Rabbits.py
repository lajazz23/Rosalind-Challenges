# Given: Positive integers n≤100 and m≤20
# Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.

def wabbits(n, m):

    rabbits = [0] * (n + 1)
    rabbits[0] = 1  

    if n >= 1:
        rabbits[1] = 1 
    if n >= 2:
        rabbits[2] = 1 
    if n >= 3:
        rabbits[3] = 2  

    for x in range(4, n + 1):
        
        rabbits[x] = rabbits[x - 1] 
        rabbits[x] += rabbits[x - 2] 

        if x - m - 1 >= 0: 
            rabbits[x] -= rabbits[x - m - 1] 

    return rabbits[n]

n = 93
m = 17
print(wabbits(n, m)) 

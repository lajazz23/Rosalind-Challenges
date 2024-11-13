# Given: A string s of length at most 200 letters and four integers a, b, c and d.
# Return: The slice of this string from indices a through b and c through d (with space in between), inclusively. In other words, we should include elements s[b] and s[d] in our slice.

# the code for the above prompt can be found below. This section was mainly me following the Rosalind tutorials.
tea_party = ['March Hare', 'Hatter', 'Dormouse', 'Alice']
tea_party[1] = 'Cheshire Cat'
tea_party.append('Jabberwocky') #to add to end of the list
print tea_party[2]

a = 'flimsy'
b = 'miserable'
c = b[0:1] + a[2:]
print c

a = 'flimsy'
b = 'miserable'
c = b[0] + a[2:]
print c

#challenge:
stist = 'bxc5fCZ78E3sTsT3oNNHyz5yJ3Ni6jIUCpkDyd3VtvAhEQPtjDQgPhrynomerusVWL6BZpJUyNTJ4IN4eAXDnPMaHbShparadoxusqGZoDoTu8C6YO2hICZW12RLdLk6w0hfjyWJdIu1jZnXPUbKrQQAaJFg3HNBnYBLNq.' #this is the string given by the Rosalind Challenge, manually inputted
a = 52
b = 62
c = 92
d = 100

output = stist[a:b+1] + '  ' +  stist[c:d+1]
print output

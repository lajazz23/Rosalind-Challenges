# Given: A file containing at most 1000 lines.
# Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.

# the code for the above prompt can be found below. This section was mainly me following the Rosalind tutorials.
f = open('input.txt', 'r')
n = 10000
f.read(n)

f.readline()

for line in f:
  print line

f = open('output.txt', 'w')
f.write('So i see')
inscription = ['Rosalind Elsie Franklin ', 1920, 1958]
s = str(inscription)
f.write(s)

for i in inscription:
  f.write(str(i) + '\n')
f.close()

# the code for the actual problem is below:
d = open('working.txt', 'r') # open the file from the computer through code, as opposed to manually inputting data.
lynuh = 1
s = open('output.txt','w')
for line in d:
    if lynuh % 2 == 0:
      s.write(str(line) + '\n')
      lynuh += 1
    else:
      lynuh += 1

d.close()
s.close()

b = open ('output.txt', 'r')
for line in b:
  print line

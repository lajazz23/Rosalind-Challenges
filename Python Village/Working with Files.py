#f = open('input.txt', 'r')
#n = 10000
#f.read(n)

#f.readline()

#for line in f:
  #print line

#f = open('output.txt', 'w')
#f.write('So i see')
#inscription = ['Rosalind Elsie Franklin ', 1920, 1958]
#s = str(inscription)
#f.write(s)

#for i in inscription:
  #f.write(str(i) + '\n')
#f.close()


d = open('working.txt', 'r')
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

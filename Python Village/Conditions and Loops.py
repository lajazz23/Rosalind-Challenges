a = 42
if a < 10:
  print 'the number is less than 10'
else:
  print 'the number is greater or equal to 10'

a = 22
b = 1
if a + b == 4:
  print 'printed when a + b equals four'
print 'always printed'

greetings = 1
while greetings <= 3:
  print 'Hello! ' * greetings
  greetings += 1 #greetings = greetings +1

  names = ['Alice', 'Bob', 'Charley']
for name in names:
  print 'Hello, ' + name

n = 10
for i in range(n):
  print i

print range(5, 12)


a = 4393
b = 9264
bruh = a
some = 0
poo = 0
for i in range(a, b+1):
    if bruh % 2 != 0:
       some += bruh # some = some + bruh
       bruh += 1
    else:
        poo += 1
        print 'poopoo' + ' ' + str(poo)
        bruh += 1
print some
       
            
    

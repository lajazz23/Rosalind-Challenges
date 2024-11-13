# Given: Two positive integers a and b (a<b<10000).
# Return: The sum of all odd integers from a through b, inclusively.

# the code for the above prompt can be found below. This section was mainly me following the Rosalind tutorials.
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

# the code for the actual problem is below:
a = 4393
b = 9264
placeholder = a
some = 0
p = 0
for i in range(a, b+1):
    if placeholder % 2 != 0:
       some += placeholder # some = some + placeholder
       placeholder += 1
    else:
        p += 1
        # print 'p' + ' ' + str(p)  # this is to make sure that the code is iterating through the loop
        placeholder += 1
print some
         
            
    

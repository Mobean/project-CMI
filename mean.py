import sys

sum = 0
n = 0

#comment

for num in open('data.txt'):
    sum += float(num)
    n += 1

print sum / n
print "Susan made this change."

import sys

sum = 0
n = 0

#comment
file_name = "data.txt'

for num in open(file_name):
    sum += float(num)
    n += 1

print sum / n
print "Susan made this change."

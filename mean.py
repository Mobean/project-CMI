import sys

sum = 0
n = 0

#comment
file_name = "data_2.txt'

for num in open('data_2.txt'):
    sum += float(num)
    n += 1

print sum / n
print "Susan made this change."

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = ""
for i in range(1):
    s = input()

s = s.split()
z = ""

for i in s:
    if (len(i)) == 3:
        z = z+"0"
    else:
        z = z+"1"
print(int(z, 2))
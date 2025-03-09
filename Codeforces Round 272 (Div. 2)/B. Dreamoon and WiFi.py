from collections import defaultdict
import math


a = input()
b = input()
a_d = {"+": 0, "-": 0}
b_d = {"+": 0, "-": 0, "?": 0}

for i in a:
    a_d[i] += 1

for i in b:
    b_d[i] += 1

if a_d["+"] < b_d["+"] or a_d["-"] < b_d["-"]:
    print(0)
else:
    useful = math.factorial(b_d["?"]) / (math.factorial(a_d["+"]-b_d["+"])  * (math.factorial(b_d["?"]-(a_d["+"] - (b_d["+"])))))
    print(useful/(2**b_d["?"]))
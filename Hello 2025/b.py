from collections import Counter
 
for _ in range(int(input())):
	a,c = map(int,input().split())
	l = Counter(input().split())
	m = len(l)
	for i in sorted(l.values()):
		if c<i:
			break
		c-=i
		m-=1
	print(max(1,m))
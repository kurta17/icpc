for _ in range(int(input())):
	n = int(input())
	dp = [0]*n
	p = n-1
	while p>=0:
		i = 0
		
		while i*i<p:
			i += 1
		x = i*i-p
		
		for k in range(x,p+1):
			dp[k] = p+x-k
		p = x-1
	print(*dp)
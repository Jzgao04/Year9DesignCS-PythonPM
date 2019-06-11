raw_input = 13254
MOD = 1000000007
for i in range(10):
	N = raw_input
	
	for j in range(2, N + 1):
		print(i)
		for k in range(1, i + 1):
			print(j)
			if j % 2 == 0:
				DP[k][0] = (DP[k - 1][1] + DP[k - 1][0]) % MOD
				DP[k + 1][0] = DP[k][0]
			else:
				DP[k][1] = ((DP[i][0] - (DP[k - 1][0] - DP[k - 1][1])) + MOD) % MOD
				DP[k + 1][1] = DP[k][1]
	print(DP[N][N % 2] % MOD)
'''
input = str(input())
for i in range(1, len(input)):
	if input[i//2==0]
'''
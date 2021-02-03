M, N = map(int,input().split())
arr = list(map(int,input().split()))
for i in range(N,len(arr),N):
	arr[N-i-1],arr[i] = arr[i], arr[N-i-1]
print(*arr,sep=" ")


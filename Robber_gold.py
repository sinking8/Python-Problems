from math import floor
arr = list(map(int,input().split()))
arr[2]*=2;arr[3]*=2
X = int(input())
arr.sort()
total = 0
try:
	total  =  floor(arr[0]/X)
	print(total)
	total  += floor(arr[1]/(arr[0]%X))
	print(total)
	total  += floor(arr[2]/(arr[1]%(arr[0]%X)))
	print(total)
	total  += floor(arr[3]/(arr[2]%(arr[1]%(arr[0]%X))))
	print(total)
except Exception:pass
finally:print(total)
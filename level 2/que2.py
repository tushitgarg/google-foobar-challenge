# Power Hungry

def solution(xs):
	n = len(xs)
	if(n==1):
		return str(xs[0])
	min_neg = -1000000
	neg_count = 0
	zero_count = 0
	prod = 1
	for i in xs:
		if(i==0):
			zero_count = zero_count + 1
			continue
		if(i<0):
			min_neg = max(min_neg,i)
			neg_count = neg_count + 1
		prod = prod*i
	if(zero_count==n):
		return str(0)
	if(neg_count & 1):
		if(neg_count == 1 and zero_count > 0 and neg_count + zero_count == n):
			return str(0)
		prod = int(prod/min_neg)

	return str(prod)

#Find the k most frequent numbers in a list of numbers
from collections import Counter
import heapq

def findKMostUsedNum(nums, k):
	count = Counter(nums)
	return heapq.nlargest(k, count.keys(), key=count.get)
	
print(findKMostUsedNum([1,3,3,6,6,7,7,7,6], 2))



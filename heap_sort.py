# 3

#Nontrivial Base Case:
	A.length = 3 # [1,2,3] 
	for i in range(1,1,-1):
		l = 1 # max_heapify
		r = 3
		largest = 2
		largest = 3
		A = [3,1,2]
		A = [3,2,1]

#Induction Case:
	A.length = n + 1 # n is already sorted
	for i in range(floor(n/2),1,stepsize=-1):
		l = A[n/2] - 1
		r = A[n/2] + 1
		# ...
		# will already be sorted until the last element
		# assume new element is larger than some elements
		l = A[n-3]
		r = A[n-1]
		largest = A[n-1]
		exchange[A[n-1],A[n-2]]
	# will iterate until the new element is not larger than its left
	# Therefore n + 1 will be sorted assuming n is.



def heap_sort(A):
	build_max_heap(A)
	for i = range(A.length,2,stepsize=-1):
		exchange(A[0],A[i])
		A.heapsize=A.heapsize-1
		max_heapify(A,1)

def build_max_heap(A):
	for i in range(floor(A.length/2),1,stepsize=-1):
		max_heapify(A,i)


def max_heapify(A,i): 
		l = left(i)
		r = right(i)
		if l <= A.heapsize and A[l] > A[i]:
			largest = l
		else:
			largest = i
		if r <= heap_size[A] and A[r] < A[largest]
			largest = r
		if largest not i:
			exchange A[i] and A[largest]
			max_heapify(A, largest)
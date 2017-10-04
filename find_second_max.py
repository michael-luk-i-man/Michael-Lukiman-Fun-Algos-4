# Michael Lukiman 
# Fundamental Algorithms
# Courant Institute of Mathematical Sciences
# HW4 2
# Find 2nd Max(A)

def find_second_max(A):
	# Assume heap is already a max heap. A[0] is first element.
	if A[2] not null:
		if A[1] >= A[2]:
			return A[1]
		else:
			return A[2]
	else:
		return A[1]		


	# Just compare the nodes of the second level from the top of the heap, 
	# which in a binary heap, are elements 2 and 3. Node 1 should already be the max.

def extract_second_max(A): 
	second_max = find_second_max(A)
	smax_location = second_max.location
	heap_increase_key(A, smax_location, smax_location)
	heap_extract_max(A)

def extract_second_max_log(A):
	second_max = find_second_max(A)
	if A.length > 2:
		smax_location = second_max.location
		if second_max.location = 1:
			A = child_tree_tip(second_max_location)
			key = A[2]
			A[1] = A[2]
			A[2] = extract_second_max_log(A) 
		elif second_max.location = 2:
			A = child_tree(second_max_location)
			key = A[1]
			A[2] = A[1]
			A[2] = extract_second_max_log(A)
	return second_max

	# recurs down the height of the tree replacing the largest child in each tree with the removed element of the previous tree. Thus, it has h operations which is log n. 

def child_tree_tip(A, i): # returns the three element child tree below
	B = A
	B[0] = B[i]
	B[1] = B[(i * 2)]
	B[2] = B[(i * 2) + 1]
	return B


def heap_increase_key(A, i, key):
	if key < A[i]:
			#err
	A[i] = key						
	while  i > 1 and A[Parent(i)] < A[i]						
		exchange A[i] and A[Parent(i)]			
		i = Parent[i]

def heap_extract_max(A):
		max = A[0]
		A[0] = A[A.length-1]
		A.length = A.length - 1
		max_heapify(A,1)


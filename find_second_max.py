# Michael Lukiman 
# Fundamental Algorithms
# Courant Institute of Mathematical Sciences
# HW4 2a
# Find 2nd Max(A)

def find_second_max(A):
	# Assume heap is already a max heap. A[0] is first element.
	if A[1] >= A[2]:
		return A[1]
	else:
		return A[2]
	# Just compare the nodes of the second level from the top of the heap, 
	# which in a binary heap, are elements 2 and 3. Node 1 should already be the max.
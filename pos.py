# Michael Lukiman
# Courant Institute of Mathematical Sciences
# Given a heap of size n, let pos = pos(A,i,n) denote the number of positive elements in the sub-heap of A rooted at i. Consider the following recursive procedure that computes pos:

# Nontrivial Base Case:
	n = 1 
	A = [1]
	positive_count(A,1,1)
	#->
	return 1
	# returns 1, as expected

# Induction Case:
	n = n + 1
	A = [1, 2, 3, ..., n + 1]
	#->
	# returns the count of positive numbers to the left of i, + 1
	# plus the the count of the positive numbers to the right of i
	# pos ends up 
	# thus, it returns the count of all positive numbers in the sub-heap

def positive_count(A,i,n): # take an Array, location i, and length n
	if i>n: # if the location index is greater than total length
		return 0 # there's no positive numbers there 
	if A[i] <= 0: # if the location index value is 0 or less
		return 0 # it's not a positive number either
	pos = positive_count(A, left(i), n) + 1 # recur until we've reached the bottom of the heap
	pos = positive_count(A,	right(i), n) + pos # recur until we tick all values to the right of index, exiting and returning 0 if there's any nonpositive number of if we've reached the end 
	return pos

# Since we run through the whole list to check for positive numbers, the amount of comparisons is on the magnitude of O(pos). 


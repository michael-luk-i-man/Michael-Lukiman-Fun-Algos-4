def pos_k(A,i,n,k): # take an Array, location i, and length n, and limit k
	if i>n: # if the location index is greater than total length
		return 0 # there's no positive numbers there 
	if A[i] <= 0: # if the location index value is 0 or less
		return 0 # it's not a positive number either
	pos = positive_count(A, left(i), n) + 1 # recur until we've reached the bottom of the heap
	if pos = k: 
		return pos
	elif: 
		pos = positive_count(A,	right(i), n) + pos # recur until we tick all values to the right of index, exiting and returning 0 if there's any nonpositive number of if we've reached the end 
	return pos

# This follows the same proof as the previous part, except now it descends through all the left most branches until the count reaches k, making two comparisons each time, after each branch checking the pos count, for a running time of magnitude O(k). Each terminal tree (with two leaves) can only add most 2 comparisons, so stopping in this regime, we will be within the range of one or two comparisons to this running time. It will stop the algorithm before seeking the number of the right branches, but continue to search those branches if k has not been reached.  
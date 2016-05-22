def PreethiPuzzle(N):
    return sum([int("1000101021"[int(c)]) for c in N])

# This problem is a map of the values 0-9 to another set of values in the range 0-9
# for each char in N add to the total sum the corresponding value to the character
# Example: 4 is 1 so 444 is equivalent to
# 4 -> 1
# 4 -> 1
# 4 -> 1
# sum=>3 <- 1+1+1
# Here is the map of the values:
# m={0:1,1:0,2:0,3:0,4:1,5:0,6:1,7:0,8:2,9:1}

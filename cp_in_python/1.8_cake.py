"""
Notes:

1. Brute Force

We have an nxn grid of rectangles.
count the area of each, and it to the appropriate
counter based on the coloring formula.

n^2 algorithm iterate through each cell, calculate each area in constant time.

2. Optimized brute force.
Count  only the cells for color 1 and 2, then subtract from total area to get amount of color 3.
Still n^2, just with a 2/3 constant factor of the above


Other notes

Each combination could be totally unique.
Does not obviouslt seem to be overlapping subproblems. Maybe a sweep?

It is a bit of a times table.
We have to avoid computing this times table altogether. that is already n^2.

Two 1d inputs, and is a geometric problem. Thinking sweep line could be good, or sliding window.
- Don't see how sorting will be useful. Messes up the geometry.
- Perhaps process 3 at a time, then fence post the end?  Can do some kind of binary_search divide and conquer.
- Split into as many 3 x 3 Blocks as possible:
- - Can't brute force this, is there a way to do it order N at the bottom?
- N work at each level of the tree
What if we turned each list into a list 3x the lenght(something about indexes, sort,) then go through them all?

Every entry is involved in a multiplcation for 0, 1, 2
ex 1:
[1, 2, 3]
[4, 5, 6]

[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6]

1s = a1 * b1 + a1*b4 +

Then the cake looks like
[4, 8, 12]
[2, 10, 15]
[ 6, 12, 18]

Questions:
all  heihgts are positive?
"""


"""

soln form book:
    Idea is reduce to 3*3 case hard fomrula, by "permuting" rows and columns. this perserves area. Runs in O(n)
"""

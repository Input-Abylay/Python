def solve(numheads, numlegs):
    r = round((numlegs - 2*numheads)/2)
    c = numheads - r
    print(c,r)
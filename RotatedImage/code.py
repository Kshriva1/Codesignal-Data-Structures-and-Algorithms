def rotateImage(a):
    a = zip(*a)
    rotated = [list(l[::-1]) for l in a]
    return rotated 

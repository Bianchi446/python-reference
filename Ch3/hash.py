# fixed() function for determining if a tuple has fixed values using hash

def fixed(o):
    try: 
        hash(o)
    except TypeError:
        return False
    return True

tm = (10, 'alpha', (1,2))
tf = (10, 'alpha', [1,2])

print(fixed(tm))
print(fixed(tf))



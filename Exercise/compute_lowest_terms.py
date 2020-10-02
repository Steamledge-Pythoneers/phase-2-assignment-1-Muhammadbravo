## TODO: complete the function "lowest_terms" below

def fraction(x, y):
    for i in range(2, y+1):
        if (x % i == 0) and (y % i == 0):
            a = int(x / i)
            b = int(y / i)
    return a, b
def lowest_terms(x):
	sp = x.split("/")
	y = fraction(int(sp[0]), int(sp[1]))
	return str(y[0]) +"/"+str(y[1])
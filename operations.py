x = 0
y = 0

def init_compl(a, ai, b, bi):
    global x
    global y
    x = complex(a, ai)
    y = complex(b, bi)

def init_ratio(a, b):
    global x
    global y
    x = float(a)
    y = float(b)

def sum():
    return x + y

def sub():
    return x - y

def mult():
    return x * y

def div():
    return x / y if y != 0 else False

def exp():
    return x**y
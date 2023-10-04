def add(a,b):
	return a+b

def subtract(a,b):
	return a+b

def test_add():
	assert add(1,1) == 2
	assert add(5.5,3.2) == 8.7

def test_subtract():
	assert subtract(1,1) == 0
	assert substract(10,-10) == 20

def double(x):
	return x * 2

data = [1, 2, 3, 4, 5]
# 関数方式
print( map(double, data) )                #=> [2, 4, 6] : 関数方式

# lambda方式
print( map(lambda x: x * 2, data) )       #=> [2, 4, 6] : 

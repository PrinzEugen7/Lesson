# 関数定義
def func(x):
	return x * 2

data = [1, 2, 3, 4, 5]

# 関数方式
map1 = map(func, data)

# lambda方式
map2 = map(lambda x: x * 2, data)

# 結果表示
print( list(map1) ) # [2, 4, 6, 8, 10]
print( list(map2) ) # [2, 4, 6, 8, 10]

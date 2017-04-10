# 関数定義
def func(x, y):
	return x + y

data = [1, 2, 3, 4, 5]

# 関数方式
reduced = reduce(func, data)

# 結果表示
print( list(reduced) ) # [1, 3, 5]

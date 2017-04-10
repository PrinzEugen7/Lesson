# 関数定義
def func(x):
	if(x%2 != 0): return True
	else: return False

data = [1, 2, 3, 4, 5]

# 関数方式
filtered = filter(func, data)

# 結果表示
print( list(filtered) ) # [1, 3, 5]

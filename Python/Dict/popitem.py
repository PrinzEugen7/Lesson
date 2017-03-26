data = {"fubuki":1, "shirayuki":2}

del_value = data.popitem()

print(del_value) # ('fubuki', 1)
print(data) # {'shirayuki': 2}

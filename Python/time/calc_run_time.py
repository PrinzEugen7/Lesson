import time

def main():
	# 開始時間
    start = time.time()
    # 計測する処理
    i = 0
    for i in range(10000):
        i = i * 2
    # 終了時間   
    end = time.time()
    # 処理時間=終了時間-開始時間
    print (end-start) # 0.00037693977356[秒]
    
if __name__ == '__main__':
	main()

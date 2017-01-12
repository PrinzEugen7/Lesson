# -*- coding: utf-8 -*-
import re

data = 'abcdefghijklmn'
pattern = re.compile(r'a.*?c') # パターン式の定義（aで始まりcで終わる最短の文字列）
match_data = pattern.match(data)# パターン式との一致判定
print( match_data.group() )  # 一致したデータを表示

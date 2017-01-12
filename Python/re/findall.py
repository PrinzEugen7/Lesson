# -*- coding: utf-8 -*-
import re

data = 'abcdefghijklmnabcdefghijklmn'
pattern = re.compile(r'd.*?g') # パターン式の定義（dで始まりgで終わる最短の文字列）
match_data = pattern.findall(data)# パターン式との一致判定
print( match_data )  # 一致したデータを表示

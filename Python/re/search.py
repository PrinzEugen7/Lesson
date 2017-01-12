# -*- coding: utf-8 -*-
import re

data = 'abcdefghijklmnabcdefghijklmn'
pattern = re.compile(r'd.*?g') # パターン式の定義（dで始まりgで終わる最短の文字列）
match_data = pattern.search(data)# パターン式との一致判定
print( match_data.group() )  # 一致したデータを表示
print( matchObj.start() ) # 一致した開始位置を表示
print( matchObj.end() )  # 一致した終了位置を表示
print( matchObj.span() )  # 一致した位置を表示

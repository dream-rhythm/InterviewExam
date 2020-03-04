# 程式語言:Python
# Python version: 3.7.3

string = "人易科技:上 機 測 驗 - 演算法"

string = string.replace(":","：")
print(f"1.把字元:改成全形 \"{string}\"")

string = string.replace(" ","").replace("-"," - ")
print(f"2.去除中文字間的空白 \"{string}\"")

string2 = string.split('：')[1].split('-')[0]
print(f"3.印出符號：到-之間得字元 \"{string2}\"")
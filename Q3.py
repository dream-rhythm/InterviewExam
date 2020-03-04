# 程式語言:Python
# Python version: 3.7.3

all = [0,1,2,3,4,5,6,7,8,9]
# 使用陣列內迭代方式加上if來過濾出想要的元素
odd = [number for number in all if number%2==1]
even = [number for number in all if number%2==0]

# 使用彙總函數sum計算總和
diff = sum(odd) - sum(even)
print(f"1.計算 奇數值總和-偶數值總和 = {diff}")
print(f"2.分割成兩個陣列 偶數值 = {even}")
print(f"                 奇數值 = {odd}")
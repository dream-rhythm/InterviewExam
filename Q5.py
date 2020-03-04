# 程式語言:Python
# Python version: 3.7.3

a = [77,5,5,22,13,55,97,4,796,1,0,9]
b = [0,1,2,3,4,5,6,7,8,9]
"""
檢查元素是否存在陣列中
由number in array去迭代待檢測陣列
如果發現元素與陣列內容相同回傳true
如果全部跑完沒發現相同，回傳false
"""
def is_in(element,array):
    for number in array:
        if element==number:
            return True
    return False

"""
交集
由element in a去迭代待檢測陣列
如果發現元素與陣列b內容相同則加入答案中
"""
def get_and(a,b):
    answer = []
    for element in a:
        if is_in(element,b):
            answer.append(element)
    return answer

"""
差集
由element in a去迭代待檢測陣列
如果發現元素與陣列b內容不同則加入答案中
"""
def get_diff(a,b):
    answer = []
    for element in a:
        if not is_in(element,b):
            answer.append(element)
    return answer
"""
聯集
先由a複製一個出一個答案陣列
由element in b去迭代待檢測陣列
如果發現元素不再答案中，則將元素加入答案中
"""
def get_or(a,b):
    answer = a.copy()
    for element in b:
        if not is_in(element,answer):
            answer.append(element)
    return answer

c = get_and(a,b)
d = get_diff(a,b)
e = get_or(a,b)

print(f"c = a 交集 b : {c}")
print(f"d = a 差集 b : {d}")
print(f"e = a 聯集 b : {e}")
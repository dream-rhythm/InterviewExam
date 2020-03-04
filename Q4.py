# 程式語言:Python
# Python version: 3.7.3

array = [77,5,5,22,13,55,97,4,796,1,0,9]

def bubblesort(arr):
    for leftLength in range(len(arr)-1,0,-1):   #剩餘待排序長度
        for index in range(leftLength):             #每次從前面開始
            if(arr[index]>arr[index+1]):                #數值大的往後移
                arr[index],arr[index+1] = arr[index+1],arr[index]
                
print(f"Before : {array}")
bubblesort(array)
print(f"After : {array}")
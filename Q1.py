# 程式語言:Python
# Python version: 3.7.3
class vehicle():
    def __init__(self,brand,type,cc,license_plate):
        self.brand = brand     #廠牌
        self.type = type    #型號
        self.cc = cc        #排氣量
        self.license_plate = license_plate #車牌號碼
        
    def getInfo(self):
        print(f"廠牌:{self.brand}")
        print(f"型號:{self.type}")
        print(f"排氣量:{self.cc}")
        print(f"車牌號碼:{self.license_plate}\n")
        
    def drive(self):
        pass
        
    def stop(self):
        pass
        
    def turn_right(self):
        pass
        
    def turn_left(self):

# car類別(繼承vehicle)
class car(vehicle):
    def drive(self):
        print("打D檔,鬆開煞車,輕踩油門")
        
    def stop(self):
        print("鬆開油門,踩煞車,車輛停妥後打P檔")
        
    def turn_right(self):
        print("順時針轉動方向盤,到達定位後方向盤回正")
        
    def turn_left(self):
        print("逆時針轉動方向盤,到達定位後方向盤回正")

# motorcycle(繼承vehicle)
class motorcycle(vehicle):
    def drive(self):
        print("鬆開煞車,轉動油門把手")
        
    def stop(self):
        print("鬆開油門把手,按下煞車")
        
    def turn_right(self):
        print("向右轉動龍頭,到達定位後龍頭回正")
        
    def turn_left(self):
        print("向左轉動龍頭,到達定位後龍頭回正")
        

"""
使用繼承時，相同處可復用父類別的程式碼(如__init__及getInfo)
並且可在父類別先建立其他程式碼呼叫時的介面
繼承後實作介面內的程式碼
可以達到相同介面，不同行為的效果
例如drive,stop,turn_right,turn_left呼叫方法一樣
卻因一個是機車，另一個是汽車而有著不同的駕駛行為
"""
# 由類別創造出實際可操作的物件
mycar = car("Ford","ranger",2000,"ABC-1234")
mymotorcycle = motorcycle("SYM","VEGA",125,"DEF-5678")

mycar.getInfo()
mymotorcycle.getInfo()

mycar.drive()
mycar.turn_right()
mycar.stop()
print()

mymotorcycle.drive()
mymotorcycle.turn_right()
mymotorcycle.stop()
print()

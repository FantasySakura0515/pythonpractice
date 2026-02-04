class Robot:
    def __init__(self, color):
        self.color = color  # 幫這個機器人漆上顏色

    def say_hi(self):
        print(f"我是{self.color}機器人，你好！")

# 蓋出一個紅色的機器人
r1 = Robot("紅色")
r1.say_hi()

# 蓋出一個藍色的機器人
r2 = Robot("藍色")
r2.say_hi()
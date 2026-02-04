class tool:
    def __init__ (self):
        self.result = 0
    
    def way (self,num):
        if num ==0:
            return (1,0)
        if num ==1:
            return (0,1)
        if num ==2:
            return (-1,0)
        if num ==3:
            return (0,-1)
        
t = tool()
length = int(input("輸入矩陣大小："))
arr = [[0 for _ in range(length)]for _ in range(length)]
x = 0
y = 0
arr[x][y] = 1
counter = 0
for i in range(2, length * length + 1):
    way = t.way(counter)
    x += way[0]
    y += way[1]
    
    turn = False
    if x==length or y==length or x<0 or y<0:
        turn = True
    elif arr[x][y] != 0:
        turn = True
    
    if turn:
        x -= way[0]
        y -= way[1]
        counter += 1
        if counter == 4: 
            counter = 0
        way = t.way(counter)
        x += way[0]
        y += way[1]
    arr[x][y] = i

for row in arr:
    # 使用 f-string 設定每個數字佔 3 格寬度並靠右對齊
    print(" ".join(f"{num:3}" for num in row))

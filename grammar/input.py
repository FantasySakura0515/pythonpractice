import math

print("這是一個二元一次方程式計算機")
print("輸入三個數值來表ax^2+bx+c=0")
a = float(input("a="))
b = float(input("b="))
c = float(input("c="))
ans1 = (-b + math.sqrt(b*b-4*a*c)) / (2*a)
ans2 = (-b - math.sqrt(b*b-4*a*c)) / (2*a)

print(f"答案為{ans1}跟{ans2}")

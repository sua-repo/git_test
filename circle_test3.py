import circle as cc

'''
def ci_circle(r) :
    print("Hello")

print(cc(4))
ci_circle(4)
'''
r = float(input("반지름 입력 : "))
ar = cc.ar_circle(r)
print("원의 넓이 :", ar)
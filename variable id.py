def modify(x):
    print("before:",id(x))
    x+=1
    print("after:",id(x))
x=32
modify(x)

def modify(lst):
    print("before:",id(lst))
    lst=lst.append(4)
    print("after:",id(lst))
lst=[1,2,3]
modify(lst)

def func_add(a,b):
    return a+b
print(func_add(3,4))

mylist1 = [3,4,5]
mylist2 = [6,7,4]
mylist3 = func_add(mylist1,mylist2)
print(mylist3)

def func_add_and_sub(a,b):
    return (a+b,a-b)
(add,sub)=func_add_and_sub(3,4)
print(add)
print(sub)
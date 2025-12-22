lambda_add = lambda a, b: a+b
print(lambda_add(3,4))

get_odd_even = lambda x: '偶数' if x %2 == 0 else '奇数'
print('2 は'+get_odd_even(2))
print('3 は'+get_odd_even(3))

mylist = range(10)
print(list (mylist))
print(list(map(lambda x:x**2,mylist)))
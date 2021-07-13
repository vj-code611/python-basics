#ordered
#immutable
#allow duplicate elements

mytuple = ("aa", 38, "vijay")
print(mytuple)

#optional para
mytuple1 = "bb", 38, "vijay"
print(mytuple1)

tp1 = tuple(["ab", 33, 22.5])
print(tp1)

print(tp1[0])
print(tp1[1])
print(tp1[2])
print(tp1[-1]) #last item
print(tp1[-2])

# tp1[0]="abc" # not supported

#single element
mytuple2 = ("aa",)
print(type(mytuple2))

#without , - its string
myStr=("aa")
print(type(myStr))


#iterate tuple
print("-----------")
for i in tp1:
	print(i)

#check item 
if 33 in tp1:
	print("yes")
else:
	print("no")

print("-----------")

tp = ('a', 'b', 'a', 'd', 'a', 'b')
print(tp)

print('len' , +len(tp))
print('count',+tp.count('a'))
# print('index',+tp.index('m')) # error-x not in tuple
print('index',+tp.index('d'))
# print('index',+tp.index('m'))  # error-x not in tuple

print("-----------")
#conversion
l = list(tp)
print(l)
print(type(l))

t = tuple(l)
print(t)
print(type(t))

print("-----------")
#slicing
a = (1, 2, 3,4, 5,6, 7, 8, 9)

b1 = a[2:6]
print(b1)

b2 = a[:4]
print(b2)

b3 = a[5:]
print(b3)

b4 = a[::2] #step
print(b4)

b5 = a[::-1] # reverse
print(b5)

b6 = a[::-2] # reverse with step 2
print(b6)


print("-----------")
#unpacking

a, b, c = "vijay", 29, 1000


print(a)
print(type(a))

print(b)
print(type(b))

print(c)
print(type(c))


print('\n -----multiple unpacking\n')
i1, *i2, i3 = (1, 2, 3, 4, 5, 6)

print(i1)
print(type(i1))

print(i2)
print(type(i2))

print(i3)
print(type(i3))

print('\n -----multiple datatype unpacking\n')
i1, *i2, i3 = (1, 2, 'a', 2.2, 'hello', 6)

print(i1)
print(type(i1))

print(i2)
print(type(i2))

print(i3)
print(type(i3))


print("-----------")


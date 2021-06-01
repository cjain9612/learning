# x=input("Enter value 1")
# a=int(x)
# y=input ("Enter value 2")
# b=int(y)
# z=a+b
# print(z)


# x = int(input("Enter value 1"))
# y = int(input("Enter value 2"))
# z = x+y
# print(z)

# ch = input('enter a char')[0]
# print(ch)




# result = eval(input('enter a function'))
# print(result)


# x = 9
# r = x%2
# if r==0:
#     print('even')
# else:
#     print('odd')
#
#

#
# x = 4
# r = x%2
# if r==0:
#     print('even')
#     if x<5:
#         print('smaller than 5')
# else:
#      print('odd')




# x = 3
# if x ==1:
#     print('one')
# elif x==2:
#     print('two')
# elif x==3:
#     print('three')
# elif x==4:
#     print('four')


# i = 1
# while i<=5:
#     print('hello')
#     i=i+1

#
# i = 5
# while i>=1:
#     print('hello')
#     i=i-1


# i = 5
# while i>=1:
#     print('hello',i)
#     i=i-1


# i = 1
# j = 1
# while i<=5:
#     print('hello')
#     i=i+1
#     while j<=5:
#         print('world')
#         j=j+1


# i = 1
# j = 1
# while i<=5:
#     print('hello')
#     while j<=5:
#         print('world')
#                                 have to complete it print hello world 5 times





# i = 1
# while i<=5:
#     print('hello',end='')
#     j=5
#     while j<=5:
#         print('world', end='')
#         j=j+1
#
#     i = i + 1
#     print()






#
# for i in range(5):
#     print(i)



#
# for i in range(5,10,1):
#     print(i)



# x = int(input('how many output'))
# i=1
# while(i<=x):
#     print(i)
#     i=i+1

# x = int(input('how many output'))
# av = 15
# i=1
# while(i<=x):
#     if(i<=av):
#         break
#         print(i)
#     i=i+1



# for i in range(1,101):
#
#     if(i%3==0):
#         continue
#
#
#     print(i)


#
# for  i in range (5):
#     for j in range(4):
#         print('#', end='')
#     print()
#
#



# for  i in range (5):
#     for j in range(i):
#         print('#', end='')
#     print()

# for  i in range (5):
#     for j in range(5-i):
#         print('#', end='')
#     print()

#
# import array as arr
#
# vals = arr.array('i',[3,4,5,6,7])
# print(vals)
#
# for e in vals:
#     print(e)



#
# import array as arr
#
# vals = arr.array('i',[3,4,5,6,7])
# print(vals)
#
# for e in vals:
#     print(e)


# import array as arr
# vals = arr.array[3,4,5,6,]
# print (vals)



# from numpy import *
# arr = array([1,3,4,5,6])
# print(arr)




# from numpy import *
# arr = array([1,2,3,4,5])
# print (arr.dtype)




#
# def first(x):
#     y =  x + 4
#     print(y)
#
# first(5)
#
#



# def sum(a,*b):
#     c=a
#     for i in b:
#         c=c+i
#     print(c)
#
#
# sum(2,6,4,3,4)


a = 0
b = 1
print(a)
print(b)
for i in range(1,10):
    c = a+b
    a = b
    b = c
    print(c)

# test 1
# a = input('Enter number of watermelon weight ')
# if int(a) %2 == 0:
#     print('yes')
# else:
#     print('no')
# test 2    
# a = input('enter a word ')
# if len(a)>10 :
#     print(f"{a[0]}{len(a)-2}{a[-1]}")
# else:
#     print(a)    
# test 3
# number_of_questions = 3
# first = [1,1,0]
# second = [1,1,1]
# third = [1,0,0]
# firstsum = sum(first)
# secondsum = sum(second)
# thirdsum = sum(third)
# a = [thirdsum,secondsum,firstsum]
# b = 0
# for i in a:
#     if i >= 2:
#        b += 1 
#     else:
#        0
# print(b)
# test 4           
# a = 0
# b = input('enter operation ++x or --x:').split()
# for i in b:
#     if i == '++x':
#        a +=1
#     elif i == '--x':
#        a -= 1
#     else:
#        print('invalid operation')
# print(a)
# test 5
# a = input('enter lenght of palce and lenght: ')
# b = int(input('enter lenght of squared plits: '))
# a = a.split()
# print(int(a[0])int(a[1])/b**2)
# test 6
# a = [
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 1, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0]
# ]
# for i in range(5):
#     for j in range(5):
#        if a[i][j] == 1:
#            print(abs(i-2)+abs(j-2))
# test 7
# a  = input('enter some letters ').lower()
# b = input('enter some letters ').lower()
# if a > b:
#     print(1)
# elif a == b:
#     print(0)
# else:
#     print(-1)
# test 8
# a = input('enter operation of sum: ').split()
# def sort(a):
#     b = len(a)-1
#     for i in range(b):
#         for j in range(0,b - i):
#             if int(a[j]) > int(a[j+2]):
#                 a[j],a[j+2] = a[j+2],a[j]
#     return a
# print(sort(a))
#test 9
# a = input('write some letters ').replace(' ','')
# b = len(a)
# if b % 2 == 0:
#     print('CHAT WITH HER!')
# else:
#     print('IGNORE HIM!')    
# test 10
# a = int(input('enter value of first banan: '))
# b = int(input('enter number how much money do you have: '))
# c = int(input('enter number how much do you want: '))
# e = a * c * (c + 1) // 2
# if e>b:
#     print(e-b)
# else:
#     print('its enough')

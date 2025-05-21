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
# test 11
# a = input('entaer any word ')
# b=sum(1 for i in a if i.isupper())
# c=sum(1 for i in a if i.islower())
# if b>c:
#     print(a.upper())
# elif b == c:
#     print('crowd of UPPER and lower letters is equal')
# else:
#     print(a.lower())  
# test 12      
# a = int(input('enter number '))
# b = int(input('enter number of tries '))
# for _ in range(b):
#     if a % 10 != 0:
#         a -= 1
#     else:
#         a //= 10
# print(a)        
# test 13
# a = input('enter any number ')
# b = set(a)
# c = 'YES'
# for i in b:
#     if i not in {'4','7'}:
#         c = 'NO'
# print(c)
# test 14
# a = input('enter how much who wins ').lower()
# b = a.count('a')
# c = a.count('d')
# if b > c:
#     print('Anton')
# elif b == c:
#     print('its imposibble because of if')
# else:
#     print('Danik')    
# test 15
# a = int(input('enter any year '))+1

# while len(set(str(a))) != len(str(a)):
#     a += 1
# print(a)
# test 16
# a = input('tipp menge von umfragenden ')
# b = input('tipp menge von antwortenden ')
# if b.count('1')>0:
#     print('HARD')
# else:
#     print('EASY')
# test 17
# a = input('enter any word ')
# b = input('enter this word conversely ')

# if a == b[::-1]:
#     print('YES')
# else:
#     print('NO')
# test 18
# a = input('enter number of friends and height of borrow: ').split()
# b = input('enter height of friends: ').split()
# wth = 0
# for i in b:
#     if int(i) >=int(a[1]):
#         wth += 2 
#     else:
#         wth += 1
# print(wth)                
# add import math and use in else wth += math.ceil(i / h)
# test 19
# n = int(input())

# current_passengers = 0
# max_passengers = 0

# for _ in range(n):
#     a, b = map(int, input().split())
#     current_passengers -= a
#     current_passengers += b
#     max_passengers = max(max_passengers, current_passengers)

# print(max_passengers)
# test 20 
# a = int(input('write number of rooms '))
# nuber_of_facilities = 0
# for _ in range(a):
#       c,d = map(int,input('enter number of current members and max memebers ').split())  
#       if d - c >=2:
#         nuber_of_facilities += 1
#       else:
#         nuber_of_facilities += 0


# print(nuber_of_facilities)        

# # ex1
# print(*[i**2 for i in range(1,int(input())+1)])

# # ex2
# print(*filter(lambda x:x%2==0,[i for i in range(int(input())+1)]))

# # ex3
# def div34(n):
#     return (num for num in range(1,n+1) if num % 3 == 0 and num%4==0)
# print(*div34(int(input())))

# # ex 4
# def squares(a,b):
#     for i in range(a,b):
#         yield i**2
# a,b = map(int,input().split())
# print(*squares(a,b))

# # ex5
# for i in range(int(input()),0,-1):
#     print(i, end=' ')
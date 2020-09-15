# 如果 a+b+c = 1000. 并且a^2 + b^2 = c^2.求a,b,c可能的组合
import time

# start_time = time.time()

# for a in range(0,1001):
#     for b in range(0,1001):
#         for c in range(0,1001):
#             if a+b+c==1000 and a**2+b**2==c**2:
#                 print(a,b,c)

# end_time = time.time()
# print(end_time-start_time)

# start_time = time.time()
# print(start_time)
# for a in range(0,1001):
#     for b in range(0,1001):
#         c = 1000 - a -b
#         if a**2+b**2==c**2:
#             print(a,b,c)


# end_time = time.time()
# print(end_time)
# print(end_time-start_time)


'''
    练习：计算前n个数的和
'''
# def sum_of_n(n):
#     start_time = time.time()
#     the_sum = 0
#     for i in range(1, n+1):
#         the_sum += i
#     end_time = time.time()
#     return the_sum,end_time-start_time

# print(sum_of_n(1000000000))

def sum_of_n(n):
    return n*(n+1)/2

start_time = time.time()
print(sum_of_n(1000000000))
end_time = time.time()
print(end_time-start_time)
"""
水仙花数：指一个三位数，它的每个位上的数字的 3次幂之和等于它本身（100 - 1000）
"""
# for i in range(100,1000):
#     #取百位
#     x = i//100
#     #取十位
#     y = (i//10)%10
#     #取个位
#     z = i%10
#     if x**3 + y**3 + z**3 == i:
#         # print(str(i)+"是水仙花数")
#         print(f"{i}是水仙花数")

"""
四叶玫瑰，a的四次方 + b的四次方 + c的四次方 + d的四次方 = abcd (1000 -10000)
"""
# for i in range(1000,10000):
#     a = i//1000
#     b = (i//100)%10
#     c = (i//10)%10
#     d = i%10
#     if a**4 + b**4 + c**4 + d**4 == i:
#         print(f"{i}是四页玫瑰")

"""
逆序输出字符串
"""
##方式1：切片方式---------------------------------------------
# a = "python"
# print(a[::-1])
##方式2：循环--------------------------------------------------
# str_info = input("请输入字符串：")
# str_list = []
# for i in range(len(str_info)-1,-1,-1):
#     str_list.append(str_info[i])
# print("".join(str_list))   ###.join()方法

"""
猜数字游戏
"""
# import random
# number = random.randint(0,100)
# for i in range(10):
#     choice = int(input("请输入你要猜测的数字"))
#     if choice > number:
#         print("你猜大了")
#     elif choice < number:
#         print("你猜小了")
#     else:
#         print("你猜对了")
#         print(f"你一共用了{i+1}次机会，数字是{choice}")
#         break
#     print(f"还剩{9-i}次机会")
# else:
#     print("10次机会已经用完，还未猜出来")
"""
百鸡百钱
"""
# count = 0
# for x in range(1,20):
#     for y in range(1,33):
#         z = 100 - x - y
#         if z > 0 and 5*x + 3*y + z/3 == 100:
#             count += 1
#             print(f"第{count}种买法，公鸡{x}只，母鸡{y}只，小鸡{z}只")

"""
润年问题：1/能被4整除，并且不能被100整除。2/能被400整除。两个条件满足任意一个就是润年
输入是否是润年
输入的是今年的第几天
"""
# year = int(input("请输入年份"))
# month = int(input("请输入月份"))
# day = int(input("请输入日期"))
# date_list = [31,29,31,30,31,30,31,31,30,31,30,31]
# count_day = day
# if year%4 == 0 and year%100 != 0 or year%400 == 0:
#     print(f"{year}是润年")
#     date_list[1] = 29
# else:
#     print(f"{year}是平年")
#     date_list[1] = 28
# for i in range(month-1):
#     count_day += date_list[i]
# print(f"{year}年{month}月{day}日是当年的第{count_day}天")


"""
猴子吃桃问题
"""
# p = 1
# print(f"第十天还剩下{p}个桃子")
# for i in range (9,0,-1):
#     p = (p+1)*2
#     print(f"第{i}天的桃子数量是{p}个")

"""
冒泡排序
"""
# import numpy as np
# pop_list = np.random.randint(100,size = 6)
# count = len(pop_list)
# print("没有排序的列表",pop_list)
# for i in range(0,count-1):
#     for j in range(count-i-1):
#         if pop_list[j] > pop_list[j+1]:   ##升序 ： >     降序  ：<
#             pop_list[j],pop_list[j+1] = pop_list[j+1],pop_list[j]
# print("排序后的列表",pop_list)

"""
选择排序
"""
import random as rd
sec_list = [rd.randint(1,100)for i in range(8)]
length = len(sec_list)
print(f"未排序的列表:{sec_list}")
for i in range(length-1):
    mid_index = i
    for j in range(i+1,length):
        if sec_list[mid_index] > sec_list[j]:
            mid_index = j
    sec_list[mid_index],sec_list[i] = sec_list[i],sec_list[mid_index]
    print(f"第{i}次循环结果{sec_list}")


"""
二分查找（有序数列）
"""
##纯算法模式
# arr_list = [5,7,11,34,73,87,94]
# number = 187
# count = 0
# left = 0
# right = len(arr_list)-1
# while left <= right:
#     middle = (left+right)//2
#     count += 1
#     if number > arr_list[middle]:
#         left = middle+1
#     elif number < arr_list[middle]:
#         right = middle-1
#     else:
#         print(f"数字{number}已经找到，索引值是{middle}")
#         break
#
# else:
#     print(f"数字{number}没有找到")
# print(f"一共查找了{count}次")

###递归函数的方式
# arr_list = [5,7,11,34,73,87,94]
# def binary_search(num,left,right):
#     if left <= right:
#         middle = (left+right)//2
#         if num < arr_list[middle]:
#             right = middle - 1
#         elif num > arr_list[middle]:
#             left  = middle + 1
#         else:
#             print(f"数字{num}已经找到，索引值是{middle}")
#             return middle
#         return binary_search(num,left,right)
#     else:
#         print(f"结束查询，{num}未找到")
#         return -1
# print(binary_search(187,0,6))
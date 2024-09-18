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


##冒泡排序

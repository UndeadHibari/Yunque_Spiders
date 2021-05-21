# 有序，0开始
# 列表是最常用的Python数据类型，它可以作为一个方括号内的逗号分隔值出现。
# 列表的数据项不需要具有相同的类型
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5 ]
list3 = ["a", "b", "c", "d"]

# 访问list元素
print("list1[2]:",list1[2])
print("list2[1:3]:",list2[1:3])  #含左不含右,便于计算长度：3-1=2，下标1开始的2个元素

# 更新列表
list3.append("e")
list3.append("e")
print(list3)
list3.remove('e')       #移除指定元素,有重复也只移除一个
del list3[1]             #按照索引删除元素
print(list3)

# 操作
print(len(list2))       #长度
print(list1+list2)      #组合
print(list1 * 4)        #重复
print(2 in list2)       #查找元素
for i in list2:
    print(i)            #迭代
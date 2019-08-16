list_so = [1,2,3,4,5]

# print("List ban đầu")
# for i in list_so:
#     print(i)

# # print(list_so[5])
# print("Độ dài của List")
# x = len(list_so) # Lấy ra độ dài của list_so
# print(x)

# print("List sau khi sửa")
# list_so[0] = 6
# for i in list_so:
#     print(i)

# del list_so[2]
# print("List sau khi bị xóa")
# for i in list_so:
#     print(i)

# print("List sau khi thêm mới")
# list_so.append(7)
# for i in list_so:
#     print(i)

sum = 0
for i in list_so:
    sum += i
print(sum)


list_so.sort() # sắp xếp từ thấp đến cao
list_so.reverse() # đảo ngược thứ tự
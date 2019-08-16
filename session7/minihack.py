
# full_name = input("Nhap ho va ten: ")
# print(full_name.upper())

# number = int(input("Nhap vao mot so: "))
# binh_phuong = number ** 2
# print("Binh phuong la: ", binh_phuong)

# from turtle import *
# shape('turtle')
# color('blue')
# d = float(input('Nhap vao ban kinh: '))
# circle(d/2)
# mainloop()

# for i in range(3, 13):
#     print(i)
#     pass

# n = int(input("Nhap n: "))
# while True:
#     if n <= 0:
#         n = int(input("Nhap n lon hon 0: "))
#     else:
#         break
#     pass

# for i in range(0, n + 1):
#     print(i)

# n = int(input("Nhap n: "))
# while True:
#     if n <= 0:
#         n = int(input("Nhap n lon hon 0: "))
#     else:
#         break
#     pass

# if n % 2 == 0:
#     n -= 1

# for i in range(n, 0, -2):
#     print(i)

# n = int(input("Nhap N: "))

# if n > 13:
#     print("So n lon hon 13")
# else:
#     print("So n khong lon hon 13")

# import datetime

# month = int(input("Nhap thang: "))

# if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
#     print("Thang nay co 31 ngay")
# elif month == 4 or month == 6 or month == 9 or month == 11:
#     print("Thang nay co 30 ngay")
# elif month == 2:
#     if datetime.datetime.now().year % 4 == 0:
#         print("Thang nay co 29 ngay")
#     else:
#         print("Thang nay co 28 ngay")
# else:
#     print("Thang nay khong co trong nam")

# user_name = input("Nhap ten dang nhap: ")
# password = input("Nhap mat khau: ")
# while True:
#     re_password = input("Nhap lai mat khau: ")
#     if password != re_password:
#         re_password = input("Nhap lai mat khau: ")
#     else:
#         break
#     pass

# while True:
#     email = input("Nhap email: ")
#     if ('@' in email) == False and ('.' in email) == False:
#         print('Email khong chua @ va .')
#         continue
#     elif len(email) <= 8:
#         print('Email khong du 8 ky tu')
#         continue
#     else:
#         hasAlpha = False
#         hasDigit = False
        
#         for charactor in email:
#             if charactor.isalpha():
#                 hasAlpha = True
#             elif charactor.isdigit():
#                 hasDigit = True
            
#             if hasAlpha == True and hasDigit == True:
#                 break
#             pass

#         if hasAlpha == True and hasDigit == True:
#             break
#         else:
#             print('Email phai chua ca chu va so')
#             continue
#     pass

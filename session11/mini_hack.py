repo_pc = {
    "HP": 20,
    "DELL": 50,
    "MACBOOK": 12,
    "ASUS": 30
}

# Hien ra so luong Macbook
print(repo_pc["MACBOOK"])

hang_may_tinh = input("Nhap hang may tinh: ")
if hang_may_tinh in repo_pc:
    print(repo_pc[hang_may_tinh])
    pass
else:
    print("Hang may tinh " + hang_may_tinh + " khong co trong kho")
    pass

repo_pc["TOSHIBA"] = 10

hang_may_tinh = input("Nhap hang may tinh moi: ")
so_luong = int(input("Nhap so luong: "))

if (hang_may_tinh in repo_pc) == False:
    repo_pc[hang_may_tinh] = so_luong
    pass
else:
    print("Hang may tinh "+ hang_may_tinh + " da ton tai")
    pass

repo_pc["DELL"] += 10
repo_pc["MACBOOK"] = 2

tong_so_luong_may = 0
for key in repo_pc:
    tong_so_luong_may += repo_pc[key]
    pass
    
print("Tong so luong may trong kho la: ", tong_so_luong_may)

repo_pc["FUJITSU"] = 15
repo_pc["ALIENWARE"] = 5

price_pc = {
    "HP": 600,
    "DELL": 650,
    "MACBOOK": 12000,
    "ASUS": 400,
    "ACER": 350,
    "TOSHIBA": 600,
    "FUJITSU": 900,
    "ALIENWARE": 1000
}

print(price_pc["ASUS"])

hang_may_tinh = input("Nhap hang may tinh: ")

if hang_may_tinh in price_pc:
    price_pc(repo_pc[hang_may_tinh])
    pass
else:
    print("Hang may tinh " + hang_may_tinh + " khong ton tai")
    pass

print("Tong gia tri don hang 5 may tinh ASUS la: ", price_pc["ASUS"] * 5)

hang_may_tinh = input("Nhap hang may tinh muon mua: ")
so_luong = int(input("Nhap so luong muon mua: "))

if hang_may_tinh in price_pc:
    print("Tong gia tri don hang {0} may tinh {1} la: {2}"
    .format(so_luong, hang_may_tinh, so_luong * price_pc[hang_may_tinh]))
    pass
else:
    print("Hang may tinh {0} khong co".format(hang_may_tinh))
    pass

hang_may_tinh = input("Nhap hang may tinh muon mua: ")
so_luong = int(input("Nhap so luong muon mua: "))
if hang_may_tinh in price_pc: #Ktra co trong menu hay k?
    if hang_may_tinh in repo_pc: #Ktra co trong kho hay k?
        if repo_pc[hang_may_tinh] >= so_luong: #Ktra so luong du hay k?
            # In tong gia tri don hang
            print("Tong gia tri don hang {0} may tinh {1} la {2}"
            .format(so_luong, hang_may_tinh, so_luong * price_pc[hang_may_tinh]))
            # Giam so luong trong kho
            repo_pc[hang_may_tinh] -= so_luong
            pass
        else:
            print("Trong kho khong du so luong may tinh can mua")
            pass
        pass
    else:
        print("Loai may tinh khong co trong kho")
        pass
    pass
else:
    print("Hay chon loai may tinh co trong menu")
    pass

order = input("Nhap hang may tinh va so luong muon mua (cach nhau boi dau :): ")
list_order = order.split(":")
hang_may_tinh = list_order[0]
so_luong = int(list_order[1])

tong_gia_tri_kho = 0
for key in repo_pc: # Lặp từng máy ở trong kho
    if key in price_pc: # Kiểm tra xem máy đó có giá không?
        # In tổng giá trị từng máy
        print("Tong gia tri cua may {0} la {1}"
        .format(key, repo_pc[key] * price_pc[key]))

        tong_gia_tri_kho += repo_pc[key] * price_pc[key]
        pass
    pass
print("Tong gia tri trong kho la: ", tong_gia_tri_kho)











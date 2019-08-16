from random import randint
width = int(input("Nhap vao chieu dai: "))
heigh = int(input("Nhap vao chieu rong: "))

# Vi tri nguoi choi
while True:
    Ph = randint(0, heigh - 1)
    Pw = randint(0, width - 1)
    Kh = randint(0, heigh - 1)
    Kw = randint(0, width - 1)
    Eh = randint(0, heigh - 1)
    Ew = randint(0, width - 1)
    # Ktra su trung nhau giua 3 diem
    if(Ph == Kh and Pw == Kw
    or Kh == Eh and Kw == Ew
    or Eh == Ph and Ew == Pw):
        continue
        pass
    else:
        break
        pass
    pass

P = {
    'h': Ph,
    'w': Pw,
    'co_chia_khoa': False
}
K = {
    'h': Kh,
    'w': Kw
}
E = {
    'h': Eh,
    'w': Ew
}
#Khoi tao map
map = []
for h in range(heigh):
    row = []
    for w in range(width):
        row.append('-')
        pass
    map.append(row)
    pass

while True:
    # In map bao gom nguoi choi
    for h in range(heigh):
        for w in range(width):
            if w == P['w'] and h == P['h']:
                print('P', end = ' ')
                pass
            elif w == K['w'] and h == K['h'] and P['co_chia_khoa'] == False:
                print('K', end = ' ')
                pass
            elif w == E['w'] and h == E['h']:
                print('E', end = ' ')
                pass
            else:
                print(map[h][w], end = ' ')
                pass
            pass
        print()
        pass

    move = input("Nhap huong di chuyen: ")
    move = move.lower()

    # Di chuyen player
    if move == 'w':
        if P['h'] != 0:
            P['h'] -= 1
            pass
        else:
            print("Ban khong the di len")
            pass
        pass
    elif move == 's':
        if P['h'] < heigh - 1:
            P['h'] += 1
            pass
        else:
            print("Ban khong the di xuong")
            pass
        pass
    elif move == 'a':
        if P['w'] != 0:
            P['w'] -= 1
            pass
        else:
            print("Ban khong the di sang trai")
            pass
        pass
    elif move == 'd':
        if P['w'] < width - 1:
            P['w'] += 1
            pass
        else:
            print("Ban khong the di sang phai")
            pass
        pass
    else:
        print("Vui long nhap huong di chuyen")
        pass

    if P['h'] == K['h'] and P['w'] == K['w']:
        print('Ban da lay duoc chia khoa')
        P['co_chia_khoa'] = True
        pass
    elif P['h'] == E['h'] and P['w'] == E['w']:
        if P['co_chia_khoa'] == False:
            print("Ban chua co chia khoa")
            pass
        else:
            print("Ban da thoat")
            break
            pass
        pass
    pass

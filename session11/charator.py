person = {
    "Name": "Light",
    "Age": 17,
    "Strength": 8,
    "Defense": 10,
    "HP": 100,
    "Backpack": ["Shield", "Bread Loaf"],
    "Gold": 100,
    "Level": 2
}

person["Gold"] += 50

person["Backpack"].append("FlintStone")

person["Pocket"] = ["MonsterDex", "Flashlight"]

list_skills = [
    {
        "Name": "Tackle",
        "Minimum level": 1,
        "Damage": 5,
        "Hit rate": 0.3
    },
    {
        "Name": "Quick attack",
        "Minimum level": 2,
        "Damage": 3,
        "Hit rate": 0.5 
    },
    {
        "Name": "Strong Kick",
        "Minimum level": 4,
        "Damage": 9,
        "Hit rate": 0.2
    }
]

# for skill in list_skills:
#     print(skill)
#     pass

print("Danh sach cac skills: ")
for index, skill in enumerate(list_skills):
    print(index + 1, skill['Name'])
    pass

from random import randint
index_skills = int(input("Chon so thu tu skills: ")) - 1
if index_skills < len(list_skills):
    # print(list_skills[index_skills])
    selected_skills = list_skills[index_skills]
    if selected_skills["Minimum level"] <= person["Level"]:
        so_ngau_nhien = randint(0, 10)
        xac_suat = so_ngau_nhien / 10
        if xac_suat > selected_skills["Hit rate"]:
            print(selected_skills["Damage"])
            pass
        else:
            print("Khong danh trung muc tieu")
            pass
        pass
    else:
        print("Khong cho phep su dung")
        pass
    pass
else:
    print("Khong co skills")
    pass




#r+ nulis jadi paling atas
"""
f = open("contoh.txt", 'w')
f.write('ini baris 1\n')
f.write('ini baris 2')
f.close()
"""

def data_user():
    user_list = []
    f = open("data_user.txt", 'r')

    for line in f:
        user_list.append(line.strip("\n"))
    f.close()

    for i in range(len(user_list)):
        user_list[i] = user_list[i].split(",")

    return user_list

def add_user(username,password, email):
    with open(data_user.txt, 'a+') as f:
        f.write(f"\n{username},{password},{email}")

users = data_user()

logged = False
while logged != True:
    users = data_user()
    print("Program login dan registrasi")
    print("1. login\n2. Registrasi")
    pil = int(input("Pilihan : "))

    if pil == 1:
        pass
    elif pil == 2:
        username = input("Masukkan username : ")
        password = 

print(users)